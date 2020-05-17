from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, QuerySet
from django.http import QueryDict
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from ._mixins import (
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin
)
from ..models import (
    Item,
    ItemSchema,
    Category
)
from ..serializers import (
    ItemSerializer,
    ItemSchemaSerializer,
    CategorySerializer,
    ItemFilterSerializer,
    ItemSchemaFilterSerializer
)


class ItemView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Item'
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    multi_query = ('schema__in',)
    filter_serializer_class = ItemFilterSerializer

    # 1-boolean_eq -> boolean_values__value
    # 3-date_gt -> datetime_values__value__gte
    # 4-choice_in -> choices_values__value__in
    # 1-text_ic -> text_values__value__icontains
    # 4-number_gt -> number_values__value__gte
    # 1.-bool_eq
    # 1.2.2-bool_eq

    queries = {
        'boolean_eq': {
            'field': 'boolean_values__field_id',
            'value': 'boolean_values__value',
            'parser': serializers.BooleanField(),
            'multi': False
        },
        'choices_in': {
            'field': 'choices_values__field_id',
            'value': 'choices_values__value__in',
            'parser': serializers.ListSerializer(
                child=serializers.CharField()
            ),
            'multi': True
        },
        'datetime_gt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__gte',
            'parser': serializers.DateTimeField(),
            'multi': False
        },
        'datetime_lt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__lte',
            'parser': serializers.DateTimeField(),
            'multi': False
        },
        'date_gt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__date__gte',
            'parser': serializers.DateField(),
            'multi': False
        },
        'date_lt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__date__lte',
            'parser': serializers.DateField(),
            'multi': False
        },
        'time_gt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__time__gte',
            'parser': serializers.TimeField(),
            'multi': False
        },
        'time_lt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__time__lte',
            'parser': serializers.TimeField(),
            'multi': False
        },
        'year_gt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__year__gte',
            'parser': serializers.IntegerField(),
            'multi': False
        },
        'year_lt': {
            'field': 'datetime_values__field_id',
            'value': 'datetime_values__value__year__lte',
            'parser': serializers.IntegerField(),
            'multi': False
        },
        'number_gt': {
            'field': 'number_values__field_id',
            'value': 'number_values__value__gte',
            'parser': serializers.FloatField(),
            'multi': False
        },
        'number_lt': {
            'field': 'number_values__field_id',
            'value': 'number_values__value__lte',
            'parser': serializers.FloatField(),
            'multi': False
        },
        'text_ic': {
            'field': 'text_values__field_id',
            'value': 'text_values__value__icontains',
            'parser': serializers.CharField(),
            'multi': False
        }
    }

    def _parse_query(self, query_text):
        parts = query_text.split('-')
        if len(parts) == 2:
            field_id, query_name = parts
            query_data = self.queries.get(query_name, None)
            if query_data is not None:
                if '.' not in field_id:
                    try:
                        field_id = int(field_id)
                        return field_id, query_data
                    except ValueError:
                        return None
                else:
                    try:
                        fields_id = field_id.split('.')
                        fields_id = [int(_id) for _id in fields_id]
                        return fields_id, query_data
                    except ValueError:
                        return None

        return None

    def _fields_queryset(
        self,
        queryset: QuerySet,
        params: QueryDict,
        schema_id: int
    ):

        # Query based only on the text fields
        text_query = params.get('query', '')
        if text_query:
            try:
                schema: ItemSchema = ItemSchema.objects.get(pk=int(schema_id))
            except (ObjectDoesNotExist, ValueError):
                raise NotFound(
                    f'ItemSchema with pk={schema_id} does not exist.'
                )

            fields = schema.query_fields

            if len(fields):
                fields_query = Q(text_values__field_id=fields[0])
                for index in range(1, len(fields)):
                    fields_query = fields_query | Q(
                        text_values__field_id=fields[index]
                    )
                queryset = queryset.filter(
                    fields_query, text_values__value__icontains=text_query
                )
            else:
                queryset = queryset.filter(
                    text_values__value__icontains=text_query
                )

        # Query based on any field
        else:
            for param in params:
                query = self._parse_query(param)
                if query is not None:
                    field_id, query_data = query
                    if query_data['multi']:
                        value = params.getlist(param)
                    else:
                        value = params.get(param)

                    value = query_data['parser'].to_internal_value(value)

                    if isinstance(field_id, int):
                        queryset = queryset.filter(Q(**{
                            query_data['field']: field_id,
                            query_data['value']: value,
                        }))
                    if isinstance(field_id, list):
                        continue

        return queryset

    def get_queryset(self):
        queryset: QuerySet = self.queryset
        params: QueryDict = self.request.query_params.copy()

        order_by = ''
        schema_id = None

        # Filter based on non-fields parameters
        if len(params):
            params_list = params.lists()
            data = {
                key: value if key in self.multi_query else value[0]
                for key, value in params_list
            }
            serializer_class = self.filter_serializer_class
            serializer = serializer_class(
                data=data,
                context={'request': self.request}
            )
            serializer.is_valid(raise_exception=True)

            params_data = serializer.data

            for key in params_data:
                params.pop(key)

            schema_id = params_data.get('schema_id', None)
            order_by = params_data.pop('order_by', '')

            queryset = queryset.filter(**params_data)

        # Filter based on fields parameters only if schema_id is specified
        if schema_id is not None:
            queryset = self._fields_queryset(queryset, params, schema_id)

        queryset = queryset.distinct()
        if order_by:
            queryset = queryset.order_by(order_by)

        return queryset


class CategoryView(
    CreateMixin,
    ListMixin,
    RetrieveMixin,
    DestroyMixin,
    UpdateMixin,
    viewsets.GenericViewSet
):

    lookup_field = 'pk'
    model_name = 'Category'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Item.objects.filter(Q(schema_id=1) & (Q(text_values__field_id=2) | Q(text_values__field_id=1)) & Q(text_values__value__icontains="abc2"))

    def get_queryset(self):
        queryset = self.queryset

        name = self.request.query_params.get('name', '')
        if name:
            queryset = queryset.filter(name__icontains=name)

        order_by = self.request.query_params.get('order_by', '')
        if order_by in ['name', 'created_at', 'updated_at']:
            queryset = queryset.order_by(order_by)

        return queryset


class ItemSchemaView(ItemView):

    model_name = 'ItemSchema'
    queryset = ItemSchema.objects.all()
    serializer_class = ItemSchemaSerializer
    multi_query = ('category_id__in',)
    filter_serializer_class = ItemSchemaFilterSerializer



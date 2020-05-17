from rest_framework import serializers


class FieldFilterSerializer(serializers.Serializer):
    item_schema_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )


class ValueFilterSerializer(serializers.Serializer):
    item_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )


class ChoiceFilterSerializer(serializers.Serializer):
    field_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )
    field__item_schema_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )


class ItemFilterSerializer(serializers.Serializer):

    order_by = serializers.CharField(required=False)

    schema_id = serializers.IntegerField(required=False)

    schema__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    created_at__lte = serializers.DateTimeField(required=False)

    created_at__gte = serializers.DateTimeField(required=False)


class ItemSchemaFilterSerializer(serializers.Serializer):

    order_by = serializers.ChoiceField(
        required=False,
        choices=[
            'name',
            'category',
            'created_at',
            'updated_at',
            '-name',
            '-category',
            '-created_at',
            '-updated_at'
        ]
    )

    name__icontains = serializers.CharField(required=False)

    category_id__in = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False
    )

    created_at__lte = serializers.DateTimeField(required=False)

    created_at__gte = serializers.DateTimeField(required=False)
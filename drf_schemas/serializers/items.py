from ._abstracts import MaskFieldSerializer, TrackTimeSerializer, JSONField
from rest_framework import serializers
from .. import models


class CategorySerializer(MaskFieldSerializer, TrackTimeSerializer):
    name = serializers.CharField(
        help_text='Category name'
    )
    description = serializers.CharField(
        help_text='Category description',
        required=False,
        allow_blank=True
    )
    parent = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all(),
        required=False,
        allow_null=True,
        help_text='Parent category ID'
    )

    class Meta:
        model = models.Category
        fields = TrackTimeSerializer.Meta.fields + (
            'id',
            'name',
            'description',
            'parent'
        )


class ItemSchemaSerializer(MaskFieldSerializer, TrackTimeSerializer):

    name = serializers.CharField(
        help_text='Schema name'
    )

    category = serializers.PrimaryKeyRelatedField(
        queryset=models.Category.objects.all(),
        required=False,
        allow_null=True,
        help_text='Schema category ID'
    )

    image = serializers.PrimaryKeyRelatedField(
        queryset=models.Image.objects.all(),
        required=False,
        allow_null=True,
        help_text='Schema image'
    )
    items_count = serializers.IntegerField(
        read_only=True,
        help_text='Number of items that belongs to this schema'
    )

    config = JSONField(required=False)

    boolean_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of boolean fields of this schema'
    )
    choices_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of choices fields of this schema'
    )
    datetime_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of datetime fields of this schema'
    )
    file_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of file fields of this schema'
    )
    images_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of images fields of this schema'
    )
    item_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of item fields of this schema'
    )
    number_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of number fields of this schema'
    )
    text_fields = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of text fields of this schema'
    )

    class Meta:
        model = models.ItemSchema
        fields = TrackTimeSerializer.Meta.fields + (
            'id',
            'name',
            'category',
            'image',
            'config',
            'items_count',
            'boolean_fields',
            'choices_fields',
            'datetime_fields',
            'file_fields',
            'images_fields',
            'item_fields',
            'number_fields',
            'text_fields',
        )


class ItemSerializer(MaskFieldSerializer, TrackTimeSerializer):

    schema = serializers.PrimaryKeyRelatedField(
        queryset=models.ItemSchema.objects.all(),
        help_text='Item schema ID'
    )

    boolean_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of boolean values of this schema'
    )

    choices_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of choices values of this schema'
    )

    datetime_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of datetime values of this schema'
    )

    file_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of file values of this schema'
    )

    images_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of images values of this schema'
    )

    item_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of item values of this schema'
    )

    number_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of number values of this schema'
    )

    text_values = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        help_text='List of text values of this schema'
    )

    represent = serializers.ListSerializer(
        child=serializers.IntegerField(),
        read_only=True
    )

    class Meta:
        model = models.Item
        fields = TrackTimeSerializer.Meta.fields + (
            'id',
            'schema',
            'boolean_values',
            'choices_values',
            'datetime_values',
            'file_values',
            'images_values',
            'item_values',
            'number_values',
            'text_values',
            'represent'
        )


# _repr_types = ('boolean', 'choices', 'datetime', 'number', 'text')
#
#
# class ItemReprSerializer(serializers.Serializer):
#
#     def to_representation(self, instance: models.Item):
#         data = []
#         for repr_type in _repr_types:
#             values = getattr(instance, f'{repr_type}_values').all()
#             for value in values:
#                 if value.field.represent:
#                     data.append(f'{repr_type}__{value.id}')
#         return data

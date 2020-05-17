from ._abstracts import MaskFieldSerializer, TrackTimeSerializer, JSONField
from rest_framework import serializers
from .. import models


class FieldSerializer(MaskFieldSerializer, TrackTimeSerializer):

    # Required
    name = serializers.CharField(
        required=True,
        help_text='Field name'
    )
    item_schema = serializers.PrimaryKeyRelatedField(
        queryset=models.ItemSchema.objects.all(),
        help_text='Schema ID this field belongs to'
    )

    # Optional
    required = serializers.BooleanField(
        required=False,
        default=True,
        help_text='Whether filling this field is mandatory on item creation'
    )
    order = serializers.IntegerField(
        required=False,
        default=0,
        help_text='Display priority of this field'
    )
    help = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text='Help text of this field to show to the user'
    )
    config = JSONField(required=False)

    class Meta:
        fields = TrackTimeSerializer.Meta.fields + (
            'name',
            'required',
            'order',
            'help',
            'item_schema',
            'config',
        )


class DateTimeFieldSerializer(FieldSerializer):

    default = serializers.DateTimeField(
        required=False,
        allow_null=True,
        help_text='Field default value'
    )
    min_value = serializers.DateTimeField(
        required=False,
        allow_null=True,
        help_text='Field minimum value'
    )
    max_value = serializers.DateTimeField(
        required=False,
        allow_null=True,
        help_text='Field maximum value'
    )

    class Meta:
        model = models.DateTimeField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'default',
            'min_value',
            'max_value'
        )


class NumberFieldSerializer(FieldSerializer):

    default = serializers.FloatField(
        required=False,
        allow_null=True,
        help_text='Field default value'
    )
    min_value = serializers.FloatField(
        required=False,
        allow_null=True,
        help_text='Field minimum value'
    )
    max_value = serializers.FloatField(
        required=False,
        allow_null=True,
        help_text='Field maximum value'
    )

    class Meta:
        model = models.NumberField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'default',
            'min_value',
            'max_value'
        )


class TextFieldSerializer(FieldSerializer):

    default = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text='Field default value'
    )
    represent = serializers.BooleanField(
        required=False,
        default=False
    )
    query = serializers.BooleanField(
        required=False,
        default=False
    )

    class Meta:
        model = models.TextField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'default',
            'represent',
            'query'
        )


class BooleanFieldSerializer(FieldSerializer):

    default = serializers.BooleanField(
        required=False,
        allow_null=True,
        help_text='Field default value'
    )

    class Meta:
        model = models.BooleanField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'default'
        )


class ChoiceSerializer(MaskFieldSerializer):

    name = serializers.CharField(
        help_text='Choice label'
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.ChoicesField.objects.all(),
        help_text='Field ID this choice belongs to'
    )

    class Meta:
        model = models.Choice
        fields = (
            'id',
            'name',
            'field'
        )


class ChoicesFieldSerializer(FieldSerializer):

    default = serializers.PrimaryKeyRelatedField(
        queryset=models.Choice.objects.all(),
        many=True,
        required=False,
        help_text='Default choices IDs'
    )
    choices = serializers.PrimaryKeyRelatedField(
        queryset=models.Choice.objects.all(),
        many=True,
        required=False,
        help_text='Allowed choices IDs'
    )
    multi = serializers.BooleanField(
        required=False,
        help_text='Whether to allow multi choice selection or not'
    )
    class Meta:
        model = models.ChoicesField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'default',
            'choices',
            'multi'
        )


class ImageSerializer(MaskFieldSerializer, TrackTimeSerializer):

    size_bytes = serializers.IntegerField(
        read_only=True,
        help_text='Image size in bytes'
    )
    height = serializers.IntegerField(
        read_only=True,
        help_text='Image height in pixels'
    )
    width = serializers.IntegerField(
        read_only=True,
        help_text='Image width in pixels'
    )

    class Meta:
        model = models.Image
        fields = TrackTimeSerializer.Meta.fields + (
            'id',
            'image',
            'size_bytes',
            'height',
            'width'
        )


class ImagesFieldSerializer(FieldSerializer):

    multi = serializers.BooleanField(
        required=False,
        help_text='Whether to allow multiple image uploads'
    )
    default = serializers.PrimaryKeyRelatedField(
        queryset=models.Image.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = models.ImagesField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'multi',
            'default'
        )


class FileSerializer(serializers.ModelSerializer, TrackTimeSerializer):

    size_bytes = serializers.IntegerField(
        read_only=True,
        help_text='File size in bytes'
    )

    class Meta:
        model = models.File
        fields = TrackTimeSerializer.Meta.fields + (
            'id',
            'file',
            'size_bytes'
        )


class FileFieldSerializer(FieldSerializer):

    multi = serializers.BooleanField(
        required=False,
        help_text='Whether to allow multiple file uploads'
    )
    default = serializers.PrimaryKeyRelatedField(
        queryset=models.File.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = models.FileField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'multi',
            'default'
        )


class ItemFieldSerializer(FieldSerializer):

    multi = serializers.BooleanField(
        required=False,
        help_text='Whether to allow multiple related items'
    )

    default = serializers.PrimaryKeyRelatedField(
        queryset=models.Item.objects.all(),
        many=True,
        required=False
    )

    target_schema = serializers.PrimaryKeyRelatedField(
        queryset=models.ItemSchema.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.ItemField
        fields = FieldSerializer.Meta.fields + (
            'id',
            'multi',
            'default',
            'target_schema'
        )

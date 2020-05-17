from ._abstracts import MaskFieldSerializer, TrackTimeSerializer
from rest_framework import serializers
from .. import models


class ValueSerializer(MaskFieldSerializer, TrackTimeSerializer):

    item = serializers.PrimaryKeyRelatedField(
        queryset=models.Item.objects.all(),
        help_text='Item ID this value belongs to'
    )

    order = serializers.IntegerField(
        read_only=True,
        help_text='Display priority of this value'
    )

    class Meta:
        fields = TrackTimeSerializer.Meta.fields + ('item', 'order')


class DateTimeValueSerializer(ValueSerializer):

    value = serializers.DateTimeField(
        required=False,
        allow_null=True,
        help_text='Field value'
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.DateTimeField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.DateTimeValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class NumberValueSerializer(ValueSerializer):

    value = serializers.FloatField(
        required=False,
        allow_null=True,
        help_text='Field value'
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.NumberField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.NumberValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class TextValueSerializer(ValueSerializer):

    value = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text='Field value',
        trim_whitespace=False
    )

    field = serializers.PrimaryKeyRelatedField(
        queryset=models.TextField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.TextValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class BooleanValueSerializer(ValueSerializer):

    value = serializers.BooleanField(
        required=False,
        allow_null=True,
        help_text='Field value'
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.BooleanField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.BooleanValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class ChoicesValueSerializer(ValueSerializer):

    value = serializers.PrimaryKeyRelatedField(
        queryset=models.Choice.objects.all(),
        many=True,
        required=False,
        help_text='Selected choices IDs'
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.ChoicesField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.BooleanValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class ImagesValueSerializer(ValueSerializer):

    value = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Image.objects.all(),
        required=False
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.ImagesField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.ImagesValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class FileValueSerializer(ValueSerializer):

    value = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.File.objects.all(),
        required=False
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.FileField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.FileValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )


class ItemValueSerializer(ValueSerializer):

    value = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Item.objects.all(),
        required=False
    )
    field = serializers.PrimaryKeyRelatedField(
        queryset=models.ItemField.objects.all(),
        help_text='Field ID this value belongs to'
    )

    class Meta:
        model = models.ItemValue
        fields = ValueSerializer.Meta.fields + (
            'id',
            'value',
            'field'
        )

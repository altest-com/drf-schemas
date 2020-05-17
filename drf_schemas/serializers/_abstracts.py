import json

from rest_framework import serializers


class MaskFieldSerializer(serializers.ModelSerializer):

    # List of fields that are serialized only if explicit required
    explicit_req = ()

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(MaskFieldSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        elif len(self.explicit_req):
            for field_name in self.explicit_req:
                self.fields.pop(field_name)

class JSONField(serializers.Field):
    default_error_messages = {
        'invalid': 'Value must be valid JSON.'
    }

    def to_internal_value(self, data):
        try:
            data = json.dumps(data)
        except (TypeError, ValueError):
            self.fail('invalid')
        return data

    def to_representation(self, value):
        try:
            value = json.loads(value)
        except (TypeError, ValueError):
            self.fail('invalid')
        return value


class TrackTimeSerializer:
    created_at = serializers.DateTimeField(
        read_only=True,
        help_text='Date and time when instance was created'
    )
    updated_at = serializers.DateTimeField(
        read_only=True,
        help_text='Date and time when instance was updated'
    )

    class Meta:
        fields = (
            'created_at',
            'updated_at'
        )
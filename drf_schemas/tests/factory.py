import shutil
from datetime import timedelta
from os import path, mkdir
from uuid import uuid4

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from faker import Faker

from ..models import (
    DateField,
    TimeField,
    DateTimeField,
    IntegerField,
    FloatField,
    CharField,
    TextField,
    BooleanField,
    ChoicesField,
    ImagesField,
    DateValue,
    TimeValue,
    DateTimeValue,
    IntegerValue,
    FloatValue,
    CharValue,
    TextValue,
    BooleanValue,
    ChoicesValue,
    ImagesValue,
    ItemSchema,
    Item
)

TZ = timezone.get_current_timezone()

FAKER = Faker()

CURR_DIR = path.abspath(path.dirname(__file__))
FACE_IMAGE_PATH = path.join(CURR_DIR, 'data/face.jpg')


def filter_keys(data: dict, keys: [list, tuple]):
    data_filtered = {}
    for key in keys:
        if key in data.keys():
            data_filtered[key] = data[key]
    return data_filtered


# def create_image_file(file_path, media_path):
#     image_name = f'face_{uuid4()}.jpg'
#     rel_path = path.join(media_path, image_name)
#     full_path = path.join(settings.MEDIA_ROOT, rel_path)
#     image = cv.imread(file_path)
#     cv.imwrite(full_path, image)
#     return rel_path


class ModelFactory:

    model_cls = None
    MODEL_REQUIRED_FIELDS = ()
    API_REQUIRED_FIELDS = ()
    API_READ_FIELDS = (
        'id',
        'created_at',
        'updated_at',
    )

    def create_instance(self, full: bool = True):
        data = self.instance_data()
        if not full:
            data = filter_keys(data, self.MODEL_REQUIRED_FIELDS)
        return self.model_cls.objects.create(**data)

    def create_instances(self, full: bool = True, count: int = 5):
        return [self.create_instance(full) for _ in range(count)]

    def instance_data(self):
        return {}

    def api_post_data(self, full: bool = True):
        data = self.instance_data()
        if not full:
            return filter_keys(data, self.API_REQUIRED_FIELDS)
        return data


class ItemSchemaFactory(ModelFactory):

    model_cls = ItemSchema
    MODEL_REQUIRED_FIELDS = ('name',)
    API_REQUIRED_FIELDS = ('name',)
    API_READ_FIELDS = ModelFactory.API_READ_FIELDS + (
        'id',
        'name',
        'date_fields',
        'time_fields',
        'datetime_fields',
        'integer_fields',
        'float_fields',
        'char_fields',
        'text_fields',
        'boolean_fields',
        'choices_fields',
        'images_fields',
    )

    def instance_data(self):
        return dict(
            name=FAKER.word()
        )


class FieldFactory(ModelFactory):

    MODEL_REQUIRED_FIELDS = ('name', 'item_schema')
    API_REQUIRED_FIELDS = ('name', 'item_schema')
    API_READ_FIELDS = ModelFactory.API_READ_FIELDS + (
        'name',
        'required',
        'order',
        'help',
        'item_schema'
    )

    def instance_data(self):
        item_schema_factory = ItemSchemaFactory()

        return dict(
            name=FAKER.word(),
            required=FAKER.pybool(),
            order=FAKER.pyint(),
            help=FAKER.sentence(),
            item_schema=item_schema_factory.create_instance()
        )

    def api_post_data(self, full: bool = True):
        data = self.instance_data().copy()
        data['item_schema'] = data['item_schema'].pk
        if not full:
            return filter_keys(data, self.API_REQUIRED_FIELDS)
        return data


class DateFieldFactory(FieldFactory):

    model_cls = DateField
    API_READ_FIELDS = FieldFactory.API_READ_FIELDS + (
        'default',
        'min_value',
        'max_value'
    )

    def instance_data(self):

        data = {}
        data.update(super().instance_data())
        data.update(dict(
            default=FAKER.date(),
            min_value=FAKER.date(),
            max_value=FAKER.date(),
        ))

        return data


class TimeFieldFactory(FieldFactory):

    model_cls = TimeField
    API_READ_FIELDS = FieldFactory.API_READ_FIELDS + (
        'default',
        'min_value',
        'max_value'
    )

    def instance_data(self):

        data = {}
        data.update(super().instance_data())
        data.update(dict(
            default=FAKER.time(),
            min_value=FAKER.time(),
            max_value=FAKER.time(),
        ))

        return data


class DateTimeFieldFactory(FieldFactory):

    model_cls = DateTimeField
    API_READ_FIELDS = FieldFactory.API_READ_FIELDS + (
        'default',
        'min_value',
        'max_value'
    )

    def instance_data(self):

        data = {}
        data.update(super().instance_data())
        data.update(dict(
            default=FAKER.iso8601(TZ),
            min_value=FAKER.iso8601(TZ),
            max_value=FAKER.iso8601(TZ),
        ))

        return data

# Generated by Django 3.0.2 on 2020-05-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_schemas', '0004_auto_20200513_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booleanfield',
            name='default',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='booleanvalue',
            name='value',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

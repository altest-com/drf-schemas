# Generated by Django 3.0.2 on 2020-04-17 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('default', models.BooleanField(blank=True, null=True)),
                ('display_as', models.CharField(choices=[('switch', 'switch'), ('buttons', 'buttons'), ('radio', 'radio')], default='switch', max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='drf_schemas.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChoicesField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('multi', models.BooleanField(blank=True, default=False)),
                ('display_as', models.CharField(choices=[('select', 'select'), ('buttons', 'buttons'), ('check', 'check')], default='select', max_length=16)),
                ('default', models.ManyToManyField(related_name='field_default', to='drf_schemas.Choice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DateTimeField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('data_type', models.CharField(choices=[('time', 'time'), ('date', 'date'), ('year', 'year'), ('month', 'month'), ('datetime', 'datetime')], default='datetime', max_length=64)),
                ('default', models.DateTimeField(blank=True, null=True)),
                ('min_value', models.DateTimeField(blank=True, null=True)),
                ('max_value', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('size_bytes', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('multi', models.BooleanField(blank=True, default=False)),
                ('default', models.ManyToManyField(related_name='defaults', to='drf_schemas.File')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='')),
                ('size_bytes', models.IntegerField(blank=True, default=0)),
                ('height', models.IntegerField(blank=True, default=0)),
                ('width', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagesField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('multi', models.BooleanField(blank=True, default=False)),
                ('default', models.ManyToManyField(related_name='defaults', to='drf_schemas.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('multi', models.BooleanField(blank=True, default=False)),
                ('default', models.ManyToManyField(related_name='field_default', to='drf_schemas.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('config', models.TextField(blank=True, default='{}')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schemas', to='drf_schemas.Category')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schema_images', to='drf_schemas.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumberField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('display_as', models.CharField(choices=[('input', 'input'), ('slider', 'slider')], default='input', max_length=16)),
                ('prefix', models.CharField(blank=True, default='', max_length=8)),
                ('suffix', models.CharField(blank=True, default='', max_length=8)),
                ('integer', models.BooleanField(blank=True, default=False)),
                ('default', models.FloatField(blank=True, null=True)),
                ('min_value', models.FloatField(blank=True, null=True)),
                ('max_value', models.FloatField(blank=True, null=True)),
                ('item_schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_fields', to='drf_schemas.ItemSchema')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(blank=True, default=True)),
                ('order', models.IntegerField(blank=True, default=0)),
                ('help', models.TextField(blank=True, default='')),
                ('config', models.TextField(blank=True, default='{}')),
                ('default', models.TextField(blank=True, default='')),
                ('rows', models.IntegerField(blank=True, default=1)),
                ('item_schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_fields', to='drf_schemas.ItemSchema')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.TextField(blank=True, default='')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_values', to='drf_schemas.TextField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_values', to='drf_schemas.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumberValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_values', to='drf_schemas.NumberField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_values', to='drf_schemas.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='drf_schemas.ItemField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_values', to='drf_schemas.Item')),
                ('value', models.ManyToManyField(related_name='target_values', to='drf_schemas.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='itemfield',
            name='item_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_fields', to='drf_schemas.ItemSchema'),
        ),
        migrations.AddField(
            model_name='itemfield',
            name='target_schema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_fields', to='drf_schemas.ItemSchema'),
        ),
        migrations.AddField(
            model_name='item',
            name='schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='drf_schemas.ItemSchema'),
        ),
        migrations.CreateModel(
            name='ImagesValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_values', to='drf_schemas.ImagesField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_values', to='drf_schemas.Item')),
                ('value', models.ManyToManyField(related_name='images_values', to='drf_schemas.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='imagesfield',
            name='item_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_fields', to='drf_schemas.ItemSchema'),
        ),
        migrations.CreateModel(
            name='FileValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_values', to='drf_schemas.FileField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_values', to='drf_schemas.Item')),
                ('value', models.ManyToManyField(related_name='file_values', to='drf_schemas.File')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='filefield',
            name='item_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_fields', to='drf_schemas.ItemSchema'),
        ),
        migrations.CreateModel(
            name='DateTimeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.DateTimeField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datetime_values', to='drf_schemas.DateTimeField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datetime_values', to='drf_schemas.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datetimefield',
            name='item_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datetime_fields', to='drf_schemas.ItemSchema'),
        ),
        migrations.CreateModel(
            name='ChoicesValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices_values', to='drf_schemas.ChoicesField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices_values', to='drf_schemas.Item')),
                ('value', models.ManyToManyField(related_name='field_values', to='drf_schemas.Choice')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='choicesfield',
            name='item_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices_fields', to='drf_schemas.ItemSchema'),
        ),
        migrations.AddField(
            model_name='choice',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='drf_schemas.ChoicesField'),
        ),
        migrations.CreateModel(
            name='BooleanValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.BooleanField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_values', to='drf_schemas.BooleanField')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_values', to='drf_schemas.Item')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='booleanfield',
            name='item_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_fields', to='drf_schemas.ItemSchema'),
        ),
    ]

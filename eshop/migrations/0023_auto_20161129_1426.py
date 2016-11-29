# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('eshop', '0022_auto_20161129_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('obj_id', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/upload')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('obj_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='images',
            name='obj_content_type',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]

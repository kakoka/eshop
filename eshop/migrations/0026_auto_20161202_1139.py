# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0025_remove_orders_catalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.SlugField(),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0013_auto_20161128_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ManyToManyField(related_name='suppliers_name', to='eshop.Suppliers'),
        ),
    ]
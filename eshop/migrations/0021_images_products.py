# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0020_auto_20161129_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop.Product'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0045_auto_20161212_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='c:\\Users\\pasha.BRE\\work\\webprojects/static/img/upload'),
        ),
    ]
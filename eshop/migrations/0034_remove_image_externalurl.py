# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0033_auto_20161208_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='externalURL',
        ),
    ]

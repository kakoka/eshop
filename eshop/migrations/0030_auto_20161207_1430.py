# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0029_auto_20161207_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='/img/'),
        ),
    ]
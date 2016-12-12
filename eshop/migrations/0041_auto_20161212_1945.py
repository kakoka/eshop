# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0040_auto_20161212_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='externalURL',
            field=models.URLField(blank=True),
        ),
        migrations.RemoveField(
            model_name='customers',
            name='address',
        ),
        migrations.AddField(
            model_name='customers',
            name='address',
            field=models.ManyToManyField(related_name='customer_address', to='eshop.Address'),
        ),
        migrations.RemoveField(
            model_name='customers',
            name='shipment',
        ),
        migrations.AddField(
            model_name='customers',
            name='shipment',
            field=models.ManyToManyField(related_name='customer_shipment', to='eshop.Shipments'),
        ),
    ]

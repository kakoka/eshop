from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from model_utils.models import StatusModel
from model_utils import Choices

# class Article(StatusModel):
#     STATUS = Choices('draft', 'published')

from eshop.models.products import Product
from eshop.models.customers import Customers, Shipments, Payments
from eshop.models.catalog import Catalog

# Таблица "Заказы"
class Orders(models.Model):
    catalog = models.ManyToManyField('Catalog', related_name="order_catalog", null=False)
    customer = models.ForeignKey('Customers')
    shipment = models.ForeignKey('Shipments')
    payment = models.ForeignKey('Payments')
    status = models.ForeignKey('OrderStatus')
    date = models.DateTimeField()
    is_payed = models.BooleanField(default=False)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __str__(self):
        return self._order

# таблица "Статус заказа"
class OrderStatus(models.Model):
    status = models.CharField(max_length=20)




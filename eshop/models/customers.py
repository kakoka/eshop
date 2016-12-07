from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from model_utils.models import StatusModel
from model_utils import Choices

# class Article(StatusModel):
#     STATUS = Choices('draft', 'published')

# таблица "Покупатели"
class Customers(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    # password - погуглить надо
    password = models.CharField(max_length=20)
    # phone - погуглить надо
    phone = models.CharField(max_length=30)
    birthdate = models.DateField()

    address = models.ManyToManyField('Address', related_name='customer_address')
    shipment = models.ManyToManyField('Shipments', related_name='customer_shipment')
    payment = models.ForeignKey('Payments')
    notes = models.TextField(blank=True, default='')
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = 'Customers'
        verbose_name_plural = 'Customers'
    def __str__(self):
        return self.firstname

# Таблица "Адрес доставки"
class Address(models.Model):
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    appartment = models.CharField(max_length=50)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.street

# Таблица "Метод доставки"
class Shipments(models.Model):
    method = models.CharField(max_length=50)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        verbose_name = 'Shipments'
        verbose_name_plural = 'Shipments'
    def __str__(self):
        return self.method


# таблица "Метод оплаты"
class Payments(models.Model):
    payment = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Paymets'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.payment

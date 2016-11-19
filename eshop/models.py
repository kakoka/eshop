from __future__ import unicode_literals

from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from model_utils.models import StatusModel
from model_utils import Choices

# class Article(StatusModel):
#     STATUS = Choices('draft', 'published')


# Таблица "Категории товаров"
class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False, editable=False, unique=True)
    un_category = models.ForeignKey('Category') #, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, unique=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __str__(self):
        return self.category_name

# таблица "Изображения товаров"
class Images(models.Model):
    images_id = models.AutoField(primary_key=True, null=False, editable=False, unique=True)
    images_name = models.ImageField(upload_to='database/img', blank=True)
    last_update = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.images_name

# таблица "Поставщики"

class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True, null=False, editable=False, unique=True)
    supplier_is_organisation = models.BooleanField(default=False)
    supplier_firstname = models.CharField(max_length=50)
    supplier_lastname = models.CharField(max_length=50)
    supplier_organization_name = models.CharField(max_length=50)
    suppliers_photo = models.ForeignKey('Images')
    supplier_email = models.EmailField(max_length=50, unique=True)
    supplier_phone = models.CharField(max_length=30)
    supplier_address = models.CharField(max_length=50)
    supplier_notes = models.TextField(blank=True, default='')
    last_update = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.supplier_id

# таблица "Товары"
class Product(models.Model):
    product_id = models.AutoField(primary_key=True, null=False, editable=False, unique=True)
    supplier_id = models.ManyToManyField('Suppliers', blank=False, related_name='suppliers')
    category_id = models.ForeignKey('Category')
    image_id = models.ForeignKey('Images', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(blank=True, default='')
    product_buy_price = models.DecimalField(max_digits=9, decimal_places=2)
    product_sell_price = models.DecimalField(max_digits=9, decimal_places=2)
    product_quantity = models.PositiveSmallIntegerField(default=0)
    last_update = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

    def __str__(self):
        return '{category} | {name} | {quantity}'.format(
            category=self.category_id,
            name=self.product_name,
            quantity=self.product_quantity
        )
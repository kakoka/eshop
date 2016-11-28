from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from model_utils.models import StatusModel
from model_utils import Choices

from eshop.models.products import Product

# Таблица "Каталог товаров"

class Catalog(models.Model):
    item = models.ForeignKey('Product')
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        pass
    def __str__(self):
        return self.id

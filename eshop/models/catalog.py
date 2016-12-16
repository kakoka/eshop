from __future__ import unicode_literals
from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField


# Таблица "Каталог товаров"

class Catalog(models.Model):
    item = models.ForeignKey('Product')
    is_OnMainPage = models.BooleanField(default=False)
    is_NewProduct = models.BooleanField(default=False)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    class Meta:
        pass
    def __str__(self):
        return str(self.id)

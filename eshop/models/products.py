from __future__ import unicode_literals
import os
from django.db import models
from django.db.models import Manager
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.conf import settings
from django.utils.safestring import mark_safe

from model_utils.models import StatusModel
from model_utils import Choices

# class Article(StatusModel):
#     STATUS = Choices('draft', 'published')


# "Категории товаров"
class CategoryManager(Manager):
    def get_queryset(self, **kwargs):
        return super(CategoryManager, self).get_queryset().all()

class Category(models.Model):
    un_category = models.ForeignKey('Category', related_name="under_category", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    objects = Manager()
    supplier_manager = CategoryManager()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name', )

    def __str__(self):
        return self.name

# "Изображения товаров"
class ImageManager(Manager):
    def get_queryset(self, **kwargs):
        return super(ImageManager, self).get_queryset().all()

class Image(models.Model):

    # name = models.SlugField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    externalURL = models.URLField(blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_obj = GenericForeignKey('content_type', 'object_id')

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    objects = Manager()
    image_manager = ImageManager()

    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.image)

    # def image_tag(self):
    #     if self.file:
    #         return u'<img src="%s" />' % self.file.url
    #     else:
    #         return '(none)'

    def save(self):
        # Don't save if there is no image (since core field is always set).
        if not self.id and not self.image:
            return
        super(Image, self).save()
    def url(self):
        if self.externalURL:
            return self.externalURL
        else:
            return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.image)))
    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    image_tag.short_description = 'Image'

class SupplierManager(Manager):
    def get_queryset(self, **kwargs):
        return super(SupplierManager, self).get_queryset().all()

# таблица "Поставщики"
class Suppliers(models.Model):
    is_organisation = models.BooleanField(default=False)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    notes = models.TextField(blank=True, default='')
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    objects = Manager()
    supplier_manager = SupplierManager()

    class Meta:
        verbose_name = 'Suppliers'
        verbose_name_plural = 'Suppliers'
        ordering = ('firstname', )

    def __str__(self):
        return self.firstname

# "Товары"

class ProductManager(Manager):
    def get_queryset(self, **kwargs):
        return super(ProductManager, self).get_queryset().all()

class Product(models.Model):

    supplier = models.ManyToManyField('Suppliers', related_name='suppliers_name', blank=False)
    category = models.ForeignKey('Category', related_name='product_category', blank=False)

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')
    buy_price = models.DecimalField(max_digits=9, decimal_places=2)
    sell_price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)

    is_InStock = models.BooleanField(default=True)
    is_OnMainPage = models.BooleanField(default=False)
    is_NewProduct = models.BooleanField(default=False)

    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    objects = Manager()
    product_manager = ProductManager()

    class Meta:
        ordering = ('name',)

    # def save(self, **kwargs):
    #     if not self.pk:
    #         print('Creating new product')
    #     else:
    #         print('Updating the existing one')
    #     super(Product, self).save(**kwargs)

    def __str__(self):
        return self.name


from django.contrib import admin
from django.utils.html import format_html
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline

#my models

from eshop.models.products import Category, Image, Suppliers, Product
from eshop.models.customers import *
from eshop.models.orders import *
from eshop.models.catalog import *

# Register your models here.

class AdminAddress(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('street', 'building', 'appartment'),
        }),
    )
    search_fields = (
        'street',
    )
    list_per_page = 50

class AdminCategory(admin.ModelAdmin):
    list_display = (
        'name',
        'un_cat',
    )
    # list_editable = (
    #     'un_cat',
    # )
    def un_cat(self, obj):
        return obj.un_category

class InlineImage(GenericTabularInline):
    model = Image
    list_display = (
        'image',

    )

class AdminProduct(admin.ModelAdmin):
    inlines = [InlineImage]
    list_display = (
        'name',
        'description',
        'is_InStock',
        'is_OnMainPage',
        'is_NewProduct',
        # 'get_image',
        'get_category',
        'get_supplier',
    )

    save_as = True

    # many-to-many
    def get_supplier(self, obj):
        return '\n'.join([d.firstname for d in obj.supplier.all()])
    # foreign key
    def get_category(self, obj):
        return obj.category.name
    # image get
    # def get_image(self, obj):
    #     return '<img src="%s">' % obj.image.first().url
    # get_image.allow_tags = True

    def get_image(self, obj):
        # return '\n'.join([d.name for d in obj.image.all()])
        #
        # return obj.image.id
        return format_html('<img src="{}" />'.format(obj.image.url))

class AdminImage(admin.ModelAdmin):
    fields = ('image_tag', 'image', 'externalURL',)
    readonly_fields = ('image_tag',)

class AdminSupplier(admin.ModelAdmin):
    list_display = (
        'firstname',
        'lastname',
        'organization_name',
        'is_organisation',
    )
    pass
    list_filter = (
        'is_organisation',
    )

class AddToCatalog(admin.StackedInline):
    model = Product
    list_display = (
        'image'
    )

#django-cart!

class AdminCatalog(admin.ModelAdmin):
    list_display = (
        'get_product',
    )
    pass
    def get_product(self, obj):
        return obj.item

        # inlines = [
    #     AddToCatalog,
    # ]

# products
admin.site.register(Category, AdminCategory)
admin.site.register(Image, AdminImage)
admin.site.register(Suppliers, AdminSupplier)
admin.site.register(Product, AdminProduct)

# catalog
admin.site.register(Catalog, AdminCatalog)

# customers
admin.site.register(Customers)
admin.site.register(Address, AdminAddress)
admin.site.register(Shipments)
admin.site.register(Payments)

# orders
admin.site.register(Orders)
admin.site.register(OrderStatus)
from django.contrib import admin
from django.utils.html import format_html
#my models

from eshop.models.products import *
from eshop.models.customers import *
from eshop.models.orders import *
from eshop.models.catalog import *

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'street',
        'building',
        'appartment',
        'created',
        'modified',
    )
    search_fields = (
        'street',
    )
    list_filter = (
        'street',
    )
    list_editable = (
        'street',
        'building',
        'appartment',
    )
    list_per_page = 50

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'un_category',
        'name',
        'created',
        'modified',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
    list_editable = (
        'un_category',
        'name',
    )
    list_per_page = 25



class AdminProduct(admin.ModelAdmin):
    list_display = (
        'get_supplier',
        'get_category',
        'name',
        'description',
        'get_image'

    )

    def get_supplier(self, obj):
        return '\n'.join([d.firstname for d in obj.supplier.all()])

    def get_category(self, obj):
        return obj.category.name

    def get_image(self, obj):
        return '\n'.join([c.image for c in obj.image.title.all()])

        # return obj.image.id
        # return format_html('<img src="{}" />'.format(obj.image.url))

    # def get_image(self, obj):
    #     return '\n'.join([d.name for d in obj.image.all()])


# products
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)
admin.site.register(Suppliers)
admin.site.register(Product, AdminProduct)

# catalog
admin.site.register(Catalog)

# customers
admin.site.register(Customers)
admin.site.register(Address, AddressAdmin)
admin.site.register(Shipments)
admin.site.register(Payments)

# orders
admin.site.register(Orders)
admin.site.register(OrderStatus)
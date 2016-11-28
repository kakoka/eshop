from django.contrib import admin

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
        'id',
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

# products
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)
admin.site.register(Suppliers)
admin.site.register(Product)

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
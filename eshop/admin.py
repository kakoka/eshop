from django.contrib import admin
from eshop.models.products import *
from eshop.models.cutomers import *
from eshop.models.orders import *
from eshop.models.catalog import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Suppliers)
admin.site.register(Product)

admin.site.register(Catalog)

admin.site.register(Customers)
admin.site.register(Address)
admin.site.register(Shipments)
admin.site.register(Payments)

admin.site.register(Orders)
admin.site.register(OrderStatus)
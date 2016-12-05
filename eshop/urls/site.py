from django.conf.urls import url
from eshop.views.products import list_products, Registration, cart


urlpatterns = [
    url(r'^$', list_products, name='list_products'),
    url(r'^cart/', cart, name='cart'),
    url(r'^reg/', Registration.as_view(), name='register'),
    # view/<int:pizza_order_id>
    # url(r'^view/(?P<pizza_order_id>[0-9]+)/', view, name='view'),
    # url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    #
    # url(r'^stats/', stats, name='stats'),
    # url(r'^/(?P<pk>[0-9]+)/$',
    #     ProductDetail.as_view(),
    #     name='product-detail'),
]

from django.conf.urls import url
from eshop.views.products import (
    main_page,
    categories,
    Registration,
    cart_add,
    cart_remove,
    cart_show,
    cart_empty,
    checkout,
)


urlpatterns = [
    url(r'^$', main_page, name='main_page'),

    url(r'^reg/$', Registration.as_view(), name='register'),
    url(r'^category/([a-zA-Z0-9_-]+)/$', categories, name='categories'),
    url(r'^cart/$', cart_show, name='cart'),
    url(r'^cart/add/$', cart_add, name='add'),
    url(r'^cart/remove/$', cart_remove, name='remove'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^cart/empty/$', cart_empty, name='show'),
    # url(r'^cart/add(?id[0-9]+)/', cart, name='cart'),
    # url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    # url(r'^stats/', stats, name='stats'),
    # url(r'^/(?P<pk>[0-9]+)/$',
    #     ProductDetail.as_view(),
    #     name='product-detail'),
]

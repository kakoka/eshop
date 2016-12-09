from django.conf.urls import url
from eshop.views.products import (
    main_page,
    categories,
    Registration,
    cart,
    add,
    remove,
)


urlpatterns = [
    url(r'^$', main_page, name='main_page'),

    url(r'^reg/', Registration.as_view(), name='register'),
    url(r'^category/([a-zA-Z0-9_-]+)/$', categories, name='categories'),
    # view/<int:pizza_order_id>
    url(r'^cart/$', cart, name='cart'),
    url(r'^cart/add/', add, name='add'),
    url(r'^cart/remove/$', remove, name='remove'),
    # url(r'^cart/show/$', show, name='show'),
    # url(r'^cart/add(?id[0-9]+)/', cart, name='cart'),

    # url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    #
    # url(r'^stats/', stats, name='stats'),
    # url(r'^/(?P<pk>[0-9]+)/$',
    #     ProductDetail.as_view(),
    #     name='product-detail'),
]

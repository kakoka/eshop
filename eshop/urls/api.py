from django.conf.urls import url
from eshop.views.api import CartList

urlpatterns = [
    # url(r'^show/', show, name='show'),
    # view/<int:pizza_order_id>
    # url(r'^view/(?P<pizza_order_id>[0-9]+)/', view, name='view'),
    # url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    #
    # url(r'^stats/', stats, name='stats'),
    url(r'^products/$', CartList.as_view(), name='cart'),
    # url(r'^list/$', list_products, name='list'),
    # url(r'^products/(?P<pk>[0-9]+)/$',
    #     views.ProductDetail.as_view(),
    #     name='product-detail'),
]

# urlpatterns = [
#     url(r'^products/$',
#         views.ProductList.as_view(),
#         name='product-list'),
#     url(r'^products/(?P<pk>[0-9]+)/$',
#         views.ProductDetail.as_view(),
#         name='product-detail'),
#     url(r'^brands/$',
#         views.BrandList.as_view(),
#         name='brand-list'),
#     url(r'^brands/(?P<pk>[0-9]+)/$',
#         views.BrandDetail.as_view(),
#         name='brand-detail'),
# ]
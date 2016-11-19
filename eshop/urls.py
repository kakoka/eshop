from django.conf.urls import url

from eshop.views import show

urlpatterns = [
    url(r'^show/', show, name='show'),
    # view/<int:pizza_order_id>
    # url(r'^view/(?P<pizza_order_id>[0-9]+)/', view, name='view'),
    # url(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name='close'),
    #
    # url(r'^stats/', stats, name='stats'),
]

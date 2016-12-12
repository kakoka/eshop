"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

# all needed urls for e-shop

import eshop.urls.site
import eshop.urls.api

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # common url for producs operations
    url(r'^products/', include('eshop.urls.site'), name='main_page'),

    # url(r'^show/', show, name='show'),
    # url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT}),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),



    # suppliers
    # url(r'^suppliers/', include('eshop.urls.suppliers')),

    # common url for api
    url(r'^api/', include('eshop.urls.api', namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        # url(r'^' + settings.MEDIA_ROOT + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        # url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     urlpatterns += url(r'^img/(?P<path>.*)$',  {'document_root': settings.MEDIA_ROOT})

#     urlpatterns.append(url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

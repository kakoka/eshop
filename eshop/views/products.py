from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Avg, Count, F
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.shortcuts import render
from eshop.models.products import Product
from eshop.models.cutomers import Customers
from eshop.models.orders import Orders
from eshop.models.catalog import Catalog

# Create your views here.

def list_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, 'eshop/index.html', {'products': products})
    return HttpResponse(status=405)

def list_customers(request):
    if request.method == "GET":
        products = Customers.objects.all()
        return render(request, 'eshop/index.html', {'products': products})
    return HttpResponse(status=405)

# def list_products(request):
#     if request.method == 'GET':
#         product = Product.objects.all()
#         if not product:
#             raise Http404
#
#         return render(request, 'eshop/list_products.html', {'product': product})
#     return HttpResponse(status=405)



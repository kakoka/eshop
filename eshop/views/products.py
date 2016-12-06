from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Avg, Count, F
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView

from django.shortcuts import render
from eshop.models.products import Product, Category
from eshop.models.customers import Customers
from eshop.models.orders import Orders
from eshop.models.catalog import Catalog

# Create your views here.

def list_products(request):
    if request.method == "GET":
        categories = Category.objects.all()
        products = Product.objects.all()
        cart = {
            "note": 'null',
            "attributes": {},
            "original_total_price": 0,
            "total_price": 0,
            "total_discount": 0,
            "total_weight": 0,
            "item_count": 0,
            "items": [],
            "requires_shipping": 'false',
        }
        return render(request, 'templatemo_045_christmas/index.html', {'cart': cart, 'products': products, 'categories': categories})
    return HttpResponse(status=405)

def cart(request):
    if request.method == "GET":
        cart = {
            "note": 'null',
            "attributes": {},
            "original_total_price": 0,
            "total_price": 0,
            "total_discount": 0,
            "total_weight": 0,
            "item_count": 0,
            "items": [],
            "requires_shipping": 'false',
        }
        return JsonResponse(cart, safe=False)
    if request.method == "POST":
        pass

def list_customers(request):
    if request.method == "GET":
        categories = Category.objects.all()
        products = Customers.objects.all()
        return render(request, 'templatemo_045_christmas/index.html', {'products': products, 'categories': categories })
        # return render(request, 'eshop/index.html', {'products': products, 'categories': categories })
    return HttpResponse(status=405)

# def list_products(request):
#     if request.method == 'GET':
#         product = Product.objects.all()
#         if not product:
#             raise Http404
#
#         return render(request, 'eshop/list_products.html', {'product': product})
#     return HttpResponse(status=405)

class Registration(FormView):
    template_name = 'eshop/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(Registration, self).form_valid(form)



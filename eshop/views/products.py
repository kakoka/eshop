from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Avg, Count, F
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView

from django.shortcuts import render
from carton.cart import Cart
from eshop.models.products import Product, Category, Image
from eshop.models.customers import Customers
from eshop.models.orders import Orders
from eshop.models.catalog import Catalog
# from django.utils import simplejson
# from jsonify.decorators import ajax_request
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# @csrf_exempt
# @ajax_request
def cart_add(request):
    if request.method == 'POST':
        q = request.POST['product_id']
        print(q)
        cart = Cart(request.session)
        product = Product.objects.get(id=request.POST['product_id'])
        cart.add(product, product.sell_price)
        print(cart.cart_serializable)
        return HttpResponse(cart.cart_serializable)

def cart_remove(request):
    if request.method == 'POST':
        q = request.POST['product_id']
        print(q)
        cart = Cart(request.session)
        product = Product.objects.get(id=request.POST['product_id'])
        cart.remove_single(product)
        return HttpResponse(cart.cart_serializable)

# @csrf_exempt
def cart_show(request):
    if request.method == "GET":
        print('get!!!')
        cart = Cart(request.session)
        return HttpResponse(cart.items_serializable)

def cart_empty(request):
    if request.method == 'GET':
        cart = Cart(request.session)
        cart.clear()
        return HttpResponse(cart.cart_serializable)

@csrf_exempt
def checkout(request):
    if request.method == 'GET':
        cart = Cart(request.session)
        return render(request, 'eshop/cart.html', {'cart': cart})

    if request.method == 'POST':
        q = request.body
        print(q)
        cart = Cart(request.session)
        return render(request, 'eshop/cart.html', {'cart': cart})

def main_page(request):
    if request.method == "GET":
        mainpage = []
        categories = Category.objects.exclude(id=1)
        # print(categories.get_categories) #.objects.get(id=1)
        products = Product.objects.all()
        for i in products:
            if i.is_OnMainPage:
                mainpage.append(i)
            if i.is_NewProduct:
                new_prod = i
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
        return render(request, 'eshop/index.html', {'newprod': new_prod, 'cart': cart, 'products': mainpage, 'categories': categories})
    return HttpResponse(status=405)

def categories(request, tag):
    if request.method == 'GET':
        categories = Category.objects.exclude(id=1)

        cat = Category.objects.filter(tag=tag).values('id')

        product = Product.objects.filter(category=cat)
        new_prod = Product.objects.get(is_NewProduct=True)

        # if not product:
        #     raise Http404
        return render(request, 'eshop/subpage.html', {'newprod': new_prod, 'products': product, 'categories': categories})
    return HttpResponse(status=405)



def list_customers(request):
    if request.method == "GET":
        categories = Category.objects.all()
        products = Customers.objects.all()
        return render(request, 'eshop/index.html', {'products': products, 'categories': categories})
        # return render(request, 'eshop/index.html', {'products': products, 'categories': categories })
    return HttpResponse(status=405)



class Registration(FormView):
    template_name = 'eshop/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(Registration, self).form_valid(form)



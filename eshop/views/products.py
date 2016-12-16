from datetime import datetime
from carton.cart import Cart
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from eshop.models.customers import Customers, Address, Shipments, Payments
from eshop.models.orders import Orders, OrderStatus
from eshop.models.products import Product, Category

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
        cart.remove(product)
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
        cart = Cart(request.session)
        cart.clear()
        params = request.POST
        params_dict = dict(params._iterlists())

        # get items list, items count and quantity from cart

        items_count = params_dict.get('itemCount')

        # lets get params for order from POST request
        for i in range(int(items_count[0])):
            r = i + 1
            prod_options = 'item_options_' + str(r)
            prod_quantity = 'item_quantity_' + str(r)

            prod_options_list = (params_dict.get(prod_options))

            key_from_list = prod_options_list[0]
            keys_extracted = key_from_list.partition(': ')

            # product id - keys_extracted
            # product quantity - quantity_extracted

            quantity_extracted = (params_dict.get(prod_quantity)[0])

            # log option
            # print('product id - ', keys_extracted[2], ', quantity - ', quantity_extracted)

            id = int(keys_extracted[2])
            quantity_extracted = int(quantity_extracted)

            # get producs from products table, add them to cart
            product = Product.objects.get(id=id)
            cart.add(product, product.sell_price, quantity=quantity_extracted)
        return render(request, 'eshop/cart.html', {'cart': cart})

def main_page(request):
    if request.method == "GET":
        mainpage = []
        categories = Category.objects.exclude(id=1)
        products = Product.objects.all()
        for i in products:
            if i.is_OnMainPage:
                mainpage.append(i)
        return render(request, 'eshop/index.html', {'products': mainpage, 'categories': categories})
    return HttpResponse(status=405)

def categories(request, tag):
    if request.method == 'GET':
        categories = Category.objects.exclude(id=1)
        cat = Category.objects.filter(tag=tag).values('id')
        product = Product.objects.filter(category=cat)
        return render(request, 'eshop/subpage.html', {'products': product, 'categories': categories})
    return HttpResponse(status=405)

def order(request):
    if request.method == "POST":
        cart = Cart(request.session)

        customer_firstname = request.POST['firstname']
        customer_lastname = request.POST['lastname']
        customer_email = request.POST['email']
        customer_phone = request.POST['phone']
        customer_address = request.POST['address']

        # get data from cart
        for i in cart.items_serializable:
            item_pk = i[0]
            item_qw = i[1]
            print(
                'product_id: ', item_pk,
                'quantity: ', item_qw.get('quantity')
            )
        # create customer
        address = Address(street=customer_address, building='12', appartment='12')
        address.save()
        shipment = Shipments.objects.get(pk=1)
        payment = Payments.objects.get(pk=1)
        customer = Customers(
            firstname=customer_firstname,
            lastname=customer_lastname,
            password='123',
            phone=customer_phone,
            birthdate='1975-10-10',
            email=customer_email,
            payment=payment
        )
        customer.save()
        customer.address.add(address)
        customer.shipment.add(shipment)
        customer.save()
        cart.clear()
        # create order!
        new_order = Orders(
            customer=customer,
            shipment=shipment,
            payment=payment,
            status=OrderStatus.objects.get(pk=1),
            date=datetime.utcnow().date(),
            is_payed=False
        )
        new_order.save()
        print(new_order.id)

        return render(request, 'eshop/order.html', {'order': new_order.id})

def list_customers(request):
    if request.method == "GET":
        categories = Category.objects.all()
        products = Customers.objects.all()
        return render(request, 'eshop/index.html', {'products': products, 'categories': categories})
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

from django.core.urlresolvers import reverse
from django.db import transaction
from django.db.models import Avg, Count, F
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.shortcuts import render
from eshop.models import Product

# Create your views here.

def show(request):
    if request.method == "GET":
        products = Product.objects.all()
        return render(request, 'eshop/index.html', {'products': products})
    return HttpResponse(status=405)


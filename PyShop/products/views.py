from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})


def new_products(request):
    return HttpResponse('New Products')

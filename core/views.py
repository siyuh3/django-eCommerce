from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

def index(request):
    context = {}
    return render(request, 'index.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

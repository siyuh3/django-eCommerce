from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')

def cart(request):
    return render(request, 'cart.html')
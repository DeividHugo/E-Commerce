from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products': products})

def login(request):
    return render(request, 'login.html')
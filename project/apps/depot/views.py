from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={'products': products})
    
@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', context={'products': products})
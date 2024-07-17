from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def categories(request):
    return render(request, 'categories.html')

def category_detail(request, category_name):

    products = Product.objects.filter(category__name=category_name)
    return render(request, 'category_detail.html', {'products': products, 'category_name': category_name})

def store_detail(request, store_name):

    products = Product.objects.filter(store__name=store_name)
    return render(request, 'store_detail.html', {'products': products, 'store_name': store_name})





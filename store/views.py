from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product

def categories(request):
    return {
        'categories':Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})


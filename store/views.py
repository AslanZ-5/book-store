from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product

def all_products(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})

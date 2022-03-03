from xml.etree.ElementInclude import include
from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import requests
import json

def all_products(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)

    return render(request, 'index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.prefetch_related("product_image").filter(category__in=category.get_descendants(include_self=True))
    context = {
            'category': category,
            'products': products,
    }
    return render(request, 'category.html', context)


def load_prducts(request):
    r = requests.get('https://fakestoreapi.com/products')

    jsonString = json.dumps(r.json())
    jsonFile = open('products.json', 'w')
    jsonFile.write(jsonString)
    jsonFile.close()
    return HttpResponse('products are loaded')


# d = {  
#     'id': 1,
#     'title': 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',
#     'price': 109.95,
#     'description': 'Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday', 
#     'category': "men's clothing", 
#     'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg', 
#     'rating': {'rate': 3.9, 'count': 120}}
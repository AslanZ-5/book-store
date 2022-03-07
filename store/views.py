from xml.etree.ElementInclude import include
from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from datetime import datetime, timedelta
import requests
import json


def all_products(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)

    return render(request, 'index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    recently_viewed = None
    if 'recently_viewed' in  request.session:
        if product.id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product.id)
        products = Product.objects.filter(id__in=request.session['recently_viewed'])
        recently_viewed = sorted(products,
        key=lambda x: request.session['recently_viewed'].index(x.id)
        )
        request.session['recently_viewed'].insert(0, product.id)  
    else:
        request.session['recently_viewed'] = [product.id]
    if len(request.session['recently_viewed']) > 5:
        request.session['recently_viewed'].pop()
    print(request.session['recently_viewed'])
    request.session.modified = True
    return render(request, 'detail.html', {'product': product, 'recently_viewed':recently_viewed})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.prefetch_related("product_image").filter(category__in=category.get_descendants(include_self=True))
    context = {
            'category': category,
            'products': products,
    }
    return render(request, 'category.html', context)



def product_filter(request):
    query = request.GET.get('q')
    products = Product.objects.filter(is_active=True)
    if query:
        time = datetime.today() - timedelta(days=6)
        products = Product.objects.prefetch_related("product_image").filter(
            Q(category__name__icontains=query)|
            Q(product_type__name__icontains=query)|
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(created_at__lte=time))
    
    context = {
           
            'products': products,
    }
    return render(request, 'category.html', context)





# d = {  
#     'id': 1,
#     'title': 'Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops',
#     'price': 109.95,
#     'description': 'Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday', 
#     'category': "men's clothing", 
#     'image': 'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg', 
#     'rating': {'rate': 3.9, 'count': 120}}
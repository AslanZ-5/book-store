from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product
from django.shortcuts import get_object_or_404



def all_products(request):
    products = Product.products.all()
    return render(request,'home.html',{'products':products})


def product_detail(request,slug):
    product = get_object_or_404(Product,slug=slug,in_stock=True)
 
    return render(request,'detail.html',{'product':product})

def category_list(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request,'category.html',context)
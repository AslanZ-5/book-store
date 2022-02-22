from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def all_products(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    context = {
            'category': category,
            'products': products,
    }
    return render(request, 'category.html', context)


def home(request):
    return HttpResponse('helllow')

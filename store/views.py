from xml.etree.ElementInclude import include
from django.shortcuts import redirect, render
from .models import Category, Product, Rating
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Count, Avg, Func
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 
from .forms import CommentForm

from datetime import datetime, timedelta
import requests
import json

class Round(Func):
  function = 'ROUND'
  template='%(function)s(%(expressions)s, 1)'



def all_products(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    paginator = Paginator(products,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'products': page_obj})


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
    request.session.modified = True


    
    if request.method == "POST":
        
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.product = product
            if request.POST.get('parent_id'):
                form.parent_id = request.POST.get('parent_id')
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
            
    else:
        form = CommentForm()
    related_products = Product.objects.filter(category=product.category)[:5]
    rating = product.rating_set.all().aggregate(stars__avg=Round(Avg('stars')), user__count=Count('user'))
    if not request.user.is_anonymous:
        if Rating.objects.filter(product=product, user=request.user).exists():
            can_rate = False
        else:
            can_rate = True 
    else:
        can_rate = False
    
    context = {
        'product': product,
        'recently_viewed':recently_viewed,
        'form':form,
        'rating':rating,
        'can_rate':can_rate,
        'related_products':related_products}
    return render(request, 'detail.html', context)

def add_stars(request):
    if not  request.user:
        return HttpResponse('You should be logged in ')
    if request.POST.get('action') == 'post_star':
            value = int(request.POST.get('value'))
            prductid = int(request.POST.get('productid'))
            rate = Rating.objects.create(product_id=prductid, user=request.user, stars=value)
            rate.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

    


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
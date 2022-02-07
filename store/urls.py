from unicodedata import name
from django.urls import path
from .views import all_products, categories,product_detail,category_list
app_name = 'store'
urlpatterns = [
    path('',all_products,name='home'),
    path('item/<slug:slug>/',product_detail,name='product_detail'),
    path('search/<slug:category_slug>/',category_list,name='category_list')
]
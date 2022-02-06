from unicodedata import name
from django.urls import path
from .views import all_products,product_detail
app_name = 'store'
urlpatterns = [
    path('',all_products,name='home'),
    path('item/<slug:slug>/',product_detail,name='product_detail')
]
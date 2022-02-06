from unicodedata import name
from django.urls import path
from .views import all_products
app_name = 'store'
urlpatterns = [
    path('',all_products,name='home'),
]
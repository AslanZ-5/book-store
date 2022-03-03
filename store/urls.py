from django.urls import path
from .views import all_products, product_detail, category_list, load_prducts
app_name = 'store'
urlpatterns = [
    path('', all_products, name='home'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', category_list, name='category_list'),
    path('load/', load_prducts, name='load')
   
]

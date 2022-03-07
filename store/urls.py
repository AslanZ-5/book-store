from django.urls import path
from .views import all_products, product_detail,  product_filter, category_list
app_name = 'store'
urlpatterns = [
    path('', all_products, name='home'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('filter/', product_filter, name='filter'),
    path('filter/<slug:category_slug>/', category_list, name='category_list')
   
   
]

from django.urls import path
from .views import (
                    all_products,
                    product_detail,
                    product_filter,
                    add_stars,
                    filter_data)
app_name = 'store'
urlpatterns = [
    path('', all_products, name='home'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('filter/', product_filter, name='filter'),
    path('filter-data', filter_data, name='filter_data' ),
    path('add/stars/', add_stars, name='add_stars' )
   
   
]

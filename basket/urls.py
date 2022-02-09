from email.mime import base
from django.urls import path
from . views import basket_summary
urlpatterns = [
    path('', basket_summary)
]
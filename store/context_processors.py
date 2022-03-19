from .models import Category, ProductType, Product
from django.db.models import Min, Max, Func


class Round(Func):
  function = 'ROUND'
  template='%(function)s(%(expressions)s, 1)'

def categories(request):
    return {
        'categories': Category.objects.filter(level=0) # level 0 is parent level of the  MPTT model
    }
def product_types(request):
    return {
        'product_types': ProductType.objects.all()
    }

def min_max_price(request):
    return {
        'max' : Product.objects.aggregate(max=Round(Max('regular_price')))
    }
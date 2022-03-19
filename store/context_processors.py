from .models import Category, ProductType


def categories(request):
    return {
        'categories': Category.objects.filter(level=0) # level 0 is parent level of the  MPTT model
    }
def product_types(request):
    return {
        'product_types': ProductType.objects.all()
    }

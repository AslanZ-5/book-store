import factory
from store.models import Category,ProductType, ProductSecification

from faker import Faker 

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = Category

    name = 'django'
    slug = 'django'


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = ProductType

    name = 'book'



class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = ProductSecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = 'pages'
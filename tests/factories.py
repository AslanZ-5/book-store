from unicodedata import category
import django
import factory
from store.models import (Category,
                         ProductType,
                         ProductSecification,
                         Product,
                         ProductSpecificationValue,)


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
        django_get_or_create = ("name",)

    name = 'book'



class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "pages"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = 'product_title'
    description = fake.text()
    slug = 'product_slug'
    regular_price = '9.99'
    discount_price = '1.11'


class ProductSpecificationValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecificationValue
    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(ProductSpecificationFactory)
    value = '100'
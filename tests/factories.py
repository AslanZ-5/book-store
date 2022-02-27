import django
import factory
from store.models import Category

from faker import Faker 

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = Category

    name = 'django'
    slug = 'django'
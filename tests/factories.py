import django
import factory
from store.models import Category
from faker import Faker

fake = Faker()


# 
# Store Factory


class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'django'
    slug = 'django'
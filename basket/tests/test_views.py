from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        self.cat1 = Category.objects.create(name='django', slug='django')
        self.user1 = User.objects.create_user(username='user1', password='test12345')
        self.prod1 = Product.objects.create(category_id=1, title='testproduct',
                                            created_by_id=1, slug='test', price=20.2, in_stock=True,
                                            is_active=True, image='django.jpg')
        self.prod2 = Product.objects.create(category_id=1, title='testproduct2',
                                            created_by_id=1, slug='test2', price=30.3, in_stock=True,
                                            is_active=True, image='django.jpg')
        self.prod3 = Product.objects.create(category_id=1, title='testproduct3',
                                            created_by_id=1, slug='test3', price=30.1, in_stock=True,
                                            is_active=True, image='django.jpg')

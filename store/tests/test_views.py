from unicodedata import name
from unittest import skip
from urllib import response 
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category,Product
from django.test import Client
from django.urls import reverse
from store.views import *
from django.http import HttpRequest
# @skip('deponstarting skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass 


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
        self.cat1 = Category.objects.create(name='django',slug='django')
        self.user1 = User.objects.create_user(username='user1',password='test12345')
        self.prod1 = Product.objects.create(category_id=1,title='testproduct',created_by_id=1,slug='test',price=2.2,in_stock=True,is_active=True,image='django.jpg')
    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code,200)
    def test_homepage_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response,'home.html')
    
    def test_product_deatil_url(self):
        response = self.c.get(reverse('store:product_detail', kwargs={'slug':'test'}))
        self.assertEqual(response.status_code,200)
    def test_category_deatil_url(self):
        response = self.c.get(reverse('store:category_list', kwargs={'category_slug':'django'}))
        self.assertEqual(response.status_code,200)

    def test_home_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>',html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code,200)

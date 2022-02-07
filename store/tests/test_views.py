from unittest import skip
from urllib import response 
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category,Product
from django.test import Client
# @skip('deponstarting skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass 


class TestViewResponse(TestCase):
    def setUp(self):
        self.c = Client()
    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code,200)
    def test_homepage_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response,'home.html')

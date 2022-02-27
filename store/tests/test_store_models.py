import pytest
from django.urls import reverse

def test_category_str(product_category):
    assert product_category.__str__() == 'django'

def test_category_reverse(client,product_category): # client allows to make ruquest 'GET'
    category = product_category
    url = reverse('store:category_list', args=[category.slug])
    response = client.get(url)
    assert response.status_code == 200



def test_producttype_str(product_type):
    assert product_type.__str__() == 'book'

def test_product_specification_str(product_specification):
    assert product_specification.__str__() == 'pages'

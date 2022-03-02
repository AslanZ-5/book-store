from urllib import response
import pytest 
from django.urls import reverse

def test_delivery_choices_page(client,customer):
    client.force_login(customer)
    response = client.get(reverse('checkout:deliverychoices'))
    assert response.status_code == 200



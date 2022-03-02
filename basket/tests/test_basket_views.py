from pydoc import cli
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_basket_summary_page(client):
    response = client.get(reverse('basket:basket_summary'))
    assert response.status_code == 200


    
    
    
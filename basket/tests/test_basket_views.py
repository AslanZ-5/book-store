from pydoc import cli, resolve
import pytest
from django.urls import reverse
from basket.basket import Basket

@pytest.mark.django_db
def test_basket_summary_page(client):
    response = client.get(reverse('basket:basket_summary'))
    assert response.status_code == 200


def test_basket(client):
    response = client.post(reverse('basket:basket_add'),{'productid':'1','productqty':'2'})
    session = Basket()
    session['aa'] = 'hellow'
    assert session['aa'] == 'hellow'



    



    
    
    
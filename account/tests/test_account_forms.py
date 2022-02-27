from pydoc import cli
import pytest
from account.forms import RegistrationForm, UserAddressForm
from django.urls import reverse
@pytest.mark.parametrize(
    "full_name, phone, address_line, address_line2, town_city, postcode, validity",
    [
        ("mike", '320204302', 'add1', 'add2', 'town', 'postcode', True),
        ("", '320204302', 'add1', 'add2', 'town', 'postcode', False),
    ]

)
def test_customer_add(full_name, phone, address_line, address_line2, town_city, postcode, validity):
    form = UserAddressForm(
        data={
            'full_name': full_name,
            'phone': phone,
            'address_line': address_line,
            'address_line2': address_line2,
            'town_city': town_city,
            'postcode': postcode,
        }
    )
    assert form.is_valid() is validity

def test_customer_create_address_unvalid_form(client,customer):
    user = customer
    client.force_login(user)
    response = client.post(reverse('account:add_address'), data={'full_name':'name'})
    assert response.status_code == 400

def test_customer_create_address_valid_form(client,customer):
    user = customer
    client.force_login(user)
    response = client.post(reverse('account:add_address'), data={
            'full_name': 'aslan',
            'phone': '3232323',
            'address_line': 'add1',
            'address_line2': 'asdd32',
            'town_city': 'Nazran',
            'postcode': '1212',
        })
    assert response.status_code == 302


@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", 'asl@gmail.com', 'test12345', 'test12345', True),
        ("user1", 'asl@gmail.com', 'test12345', '', False), # no second password
        ("user1", 'asl@gmail.com', 'tast123345', 'test12345', False), # password mismatch
        ("user1", '', 'test12345', 'test12345', False), # no email
        ("user1", 'ad.com', 'test12345', 'test12345', False), # incorrect email
    ]
)
@pytest.mark.django_db
def test_create_account(user_name, email, password, password2, validity):
    form = RegistrationForm(
        data={
            'user_name': user_name,
            'email': email,
            'password': password,
            'password2': password2
        
        }
    )
    assert form.is_valid() is validity


@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", 'asl@gmail.com', 'test12345', 'test12345', 200),
        ("user1", '', 'test12345', '', 400), # no email
        ("user1", 'asl@gmail.com', 'tast123345', 'test12345', 400), # password mismatch
    
    ]
)
@pytest.mark.django_db
def test_create_account_view(client, user_name, email, password, password2, validity):
    response = client.post(reverse('account:register'),
        data={
            'user_name': user_name,
            'email': email,
            'password': password,
            'password2': password2
        
        }
    )
    assert response.status_code == validity

def test_account_register_redirect(client,customer):
    user = customer
    client.force_login(user)
    response = client.get(reverse('account:register'))
    assert response.status_code == 302

def test_account_register_page(client,customer):
    response = client.get(reverse('account:register'))
    assert response.status_code == 200

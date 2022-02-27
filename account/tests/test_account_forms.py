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

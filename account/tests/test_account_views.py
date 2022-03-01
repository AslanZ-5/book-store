import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_add_to_wish_list(client,customer,product):
    # referer = 'http://localhost:8000/{}'.format(product.get_absolute_url())
    id = product.id
    client.force_login(customer)

    # response = client.post(reverse('account:add_to_wishlist',args=[id]))
    assert product.users_wishlist.count() == 0


def test_wish_list_page(client,customer):
    client.force_login(customer)
    response = client.get(reverse('account:wishlist'))

    assert response.status_code == 200

def test_dashboard_page(client,customer):
    client.force_login(customer)
    response = client.get(reverse('account:dashboard'))

    assert response.status_code == 200

@pytest.mark.parametrize(
    "email, first_name, validity",
    [
        ('a@a.com','ddssd', 200),
        ('a@ddc.com','ddd',400)
    ]
)
def test_user_edit_post_page(client, customer, email, first_name, validity):
    client.force_login(customer)
    response = client.post(reverse('account:edit_details'),
     data={
         'email':email,
         'first_name':first_name
         })
    assert response.status_code == validity
    
def test_user_edit_get_page(client, customer):
    client.force_login(customer)
    response = client.get(reverse('account:edit_details'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_delete_page(client, customer):
    client.force_login(customer)
    response = client.post(reverse('account:delete_user'))
    assert response.status_code == 302

def test_account_view_address_get_page(client, customer):
    client.force_login(customer)
    response = client.get(reverse('account:addresses'))
    assert response.status_code == 200

def test_account_add_address_get_page(client, customer):
    client.force_login(customer)
    response = client.get(reverse('account:add_address'))
    assert response.status_code == 200    

# @pytest.mark.django_db
# def test_account_edit_address_post_page(client, customer,address):
#     client.force_login(customer)
#     response = client.post(reverse('account:edit_address', address.id),
#     data={
#         "full_name":'mike',
#          "phone":'123234234',
#           "address_line":'32',
#            "address_line2":'ddd',
#             "town_city":'naz',
#              "postcode":'332'
#         })
#     print(response.status_code)

@pytest.mark.django_db
def test_account_edit_address_get_page(db,client, customer,address):
    client.force_login(customer)
    print(address.customer)
    # response = client.get(reverse('account:edit_address',args=[address.id]))
    
import pytest

def test_custormer_str(customer):
    assert customer.__str__() == 'user1'

def test_custormer_str(adminuser):
    assert adminuser.__str__() == 'admin_user'


def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email='')
    assert str(e.value) == 'Customer Account: You must provide an email address'

def test_customer_email_incorrect_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email='dddd.com')
    assert str(e.value) == "You must provide an email address"


def test_adminuser_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email='', is_superuser=True, is_staff=True)
    assert str(e.value) == 'Superuser Account: You must provide an email address'

def test_adminuser_email_incorrect_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email='dddd.com', is_superuser=True, is_staff=True)
    assert str(e.value) == "You must provide an email address"

def test_adminuser_is_staff_false(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(is_staff=False, is_superuser=True)
    assert str(e.value) == 'Superuser must be assigned to is_staff=True.'

def test_adminuser_is_superuser_false(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(is_superuser=False,is_staff=True)
    assert str(e.value) == 'Superuser must be assigned to is_superuser=True.'

def test_address_str(address):
    assert address.__str__() == "Address"
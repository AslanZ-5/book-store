import pytest
from pytest_factoryboy import register
from tests.factories import (

    CategoryFactory,
    ProductFactory,
    ProductTypeFactory,
    ProductSpecificationFactory,
    ProductSpecificationValueFactory,
    CustomerFactory,
    AddressFactory,
    DeliveryOptionsFactory,
    PaymentSelectionsFactory,

    
)

register(CategoryFactory)
register(ProductTypeFactory)
register(ProductSpecificationFactory)
register(ProductFactory)
register(ProductSpecificationValueFactory)
register(CustomerFactory)
register(AddressFactory)
register(DeliveryOptionsFactory)
register(PaymentSelectionsFactory)



@pytest.fixture
def product_category(db,category_factory):
    category = category_factory.create()
    return category

@pytest.fixture
def product_type(db,product_type_factory):
    product_type = product_type_factory.create()
    return product_type

@pytest.fixture
def product_specification(db, product_specification_factory):
    product_spec = product_specification_factory.create()
    return product_spec

@pytest.fixture
def product(db,product_factory):
    product = product_factory.create()
    return product
    
@pytest.fixture
def product_spec_value(db, product_specification_value_factory):
    product_spec_value = product_specification_value_factory.create()
    return product_spec_value

@pytest.fixture
def customer(db, customer_factory):
    new_customer = customer_factory.create()
    return new_customer

@pytest.fixture
def adminuser(db, customer_factory):
    new_customer = customer_factory.create(name='admin_user', email='dd@dd.com', is_staff=True, is_superuser=True)
    return new_customer

@pytest.fixture
def address(db, address_factory):
    new_address = address_factory.create()
    return new_address


@pytest.fixture
def delivery_option(db, delivery_options_factory):
    delivery_option = delivery_options_factory.create()
    return delivery_option


@pytest.fixture
def delivery_selection(db, payment_selections_factory):
    delivery_selection = payment_selections_factory.create()
    return delivery_selection

# def order(db,order_factory):
#     order = order_factory.create()
#     return order
from pyparsing import ParseSyntaxException
import pytest 


def test_DeliveryOptions_str(delivery_option):
    assert delivery_option.__str__() == 'fastdl'


def test_delivery_selection_str(delivery_selection):
    assert delivery_selection.__str__() == 'paypal'
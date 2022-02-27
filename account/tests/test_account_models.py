import pytest

def test_custormer_str(customer):
    assert customer.__str__() == 'user1'
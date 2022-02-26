
import pytest


def test_hello_world(test_fixture1):
    print('fix_func')
    assert test_fixture1 == 1

@pytest.mark.xfail
def test_hello_world2(test_fixture1):
    print('fix_func2')
    assert test_fixture1 == 3
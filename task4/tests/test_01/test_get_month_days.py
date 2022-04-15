from simple_library_01.functions import get_month_days
import pytest


def test_get_month_days_1930():
    assert 30 == get_month_days(1930, 2)


def test_get_month_days_simple_leap():
    assert 29 == get_month_days(2020, 2)


def test_get_month_days_simple_unleap():
    assert 28 == get_month_days(2021, 2)


def test_get_month_days_simple_30():
    assert 30 == get_month_days(2020, 6)


def test_get_month_days_simple_31():
    assert 31 == get_month_days(2020, 5)


def test_get_month_days_simple_err():
    with pytest.raises(AttributeError) as e:
        get_month_days(2003, 18)
    message = e.value.args[0]
    assert message == 'Month should be in range [1-12]'

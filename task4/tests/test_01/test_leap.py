from simple_library_01.functions import is_leap
import pytest


def test_is_leap_True():
    assert True == is_leap(2020)


def test_is_leap_False():
    assert False == is_leap(2022)


def test_is_leap_Err():
    with pytest.raises(AttributeError) as exc:
        is_leap(-1)
    msg = exc.value.args[0]
    assert msg == 'Year must be greater than 0'


def test_is_leap_2500():
    assert False == is_leap(2500)


def test_is_leap_1200():
    assert True == is_leap(1200)


def test_is_leap_float():
    assert False == is_leap(125.5)
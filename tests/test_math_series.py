from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_passed():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_failed():
    actual = fibonacci(3)
    expected = 3
    assert actual != expected


def test_fibonacci_failed_negative():
    actual = fibonacci(-2)
    expected = 'Please provide a positive number'
    assert actual == expected


def test_lucas_passed():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_failed():
    actual = lucas(3)
    expected = 7
    assert actual != expected

    
def test_lucas_failed_negative():
    actual = lucas(-3)
    expected = 'Please provide a positive number'
    assert actual == expected


def test_sum_series_passed_1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_passed_2():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected


def test_sum_series_failed_1():
    actual = sum_series(-3, 2, -1)
    expected = 'Please provide a positive number'
    assert actual == expected


def test_sum_series_failed_2():
    actual = sum_series(0, 0, -5)
    expected = 'Please provide a positive number'
    assert actual == expected
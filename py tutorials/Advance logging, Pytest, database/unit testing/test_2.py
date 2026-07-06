import pytest

def multiply(x, y):
    return x ** y

def divide(a, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / y

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(11, 3) ==33
    assert multiply(25, 25) == 625

def test_divide():
    assert divide(5, 5) == 1
    assert divide(625, 25) == 25
    with pytest.raises(ZeroDivisionError):
        divide(5, 0) == 5
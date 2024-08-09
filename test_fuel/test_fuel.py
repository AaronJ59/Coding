from fuel import convert
from fuel import gauge
import pytest


def test_both():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/10") == 10 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(20) == "20%"

def test_zeroDivison():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_valueError():
    with pytest.raises(ValueError):
        convert("pizza/dog")
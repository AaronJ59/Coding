from working import convert
import pytest



def test_correct_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_incorrect_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_outofrange_hours():
    with pytest.raises(ValueError):
        convert("4 AM to 18 PM")

def test_outofrange_minutes():
    with pytest.raises(ValueError):
        assert convert("3:60 AM to 8:60 PM")


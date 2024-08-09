from numb3rs import validate


def test_ip():
    assert validate(r"29.64.32.19") == True
    assert validate(r"79.3.8") == False
    assert validate(r"22.28") == False
    assert validate(r"43") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"693.1.29.45") == False
    assert validate(r"1.893.61.16") == False
    assert validate(r"123.15.903.98") == False
    assert validate(r"11.12.13.798") == False

def test_letters():
    assert validate(r"cat") == False
    assert validate(r"dog") == False






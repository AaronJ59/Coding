from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.cookiejarcapacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.cookiejar_with_deposit == 5
    jar.deposit(3)
    assert jar.cookiejar_with_deposit == 8
    jar.deposit(2)
    assert jar.cookiejar_with_deposit == 10

    jar = Jar(12)
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar = Jar(7)
    with pytest.raises(ValueError):
        jar.deposit(9)

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.cookiejar_with_deposit == 5








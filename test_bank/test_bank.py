from bank import value


def test_zero():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello bAtmAn") == 0
    assert value("hello boy") == 0
def test_twenty():
    assert value("Hey man") == 20
    assert value("Howdy jacobs") == 20
    assert value("Hey BroS") == 20
def test_onehundred():
    assert value("yo") == 100
    assert value("jack") == 100

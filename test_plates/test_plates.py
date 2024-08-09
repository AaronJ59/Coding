from plates import is_valid

def test_zeroAsFirstNum():
     assert is_valid("CS05") == False
     assert is_valid("cS05") == False
def test_wrongcharacter():
     assert is_valid("PI3.14") == False
def test_toolittle():
     assert is_valid("H") == False
def test_toobig():
     assert is_valid("OUTATIME") == False
def test_numberinmiddle():
     assert is_valid("PE12GR") == False
def test_correctplate():
     assert is_valid("CS50") == True
     assert is_valid("HEY42") == True
def test_startswithtwoletters():
     assert is_valid("AA") == True
     assert is_valid("A2") == False

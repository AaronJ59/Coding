import pytest
from seasons import minutes_to_days, days_to_min_in_words, Time


def test_minutes_to_days():
    time = Time("2005-09-22")
    assert minutes_to_days(time) == "6613"


def test_time_initialization():
    time = Time("2005-09-22")
    assert time.year == 2005
    assert time.month == 9
    assert time.day == 22


def test_days_to_min_in_words():
    assert days_to_min_in_words("6613") == "Nine million, five hundred twenty-two thousand, seven hundred twenty minutes"
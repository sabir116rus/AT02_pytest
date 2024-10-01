import pytest
from main import count_vowels

def test_all_vowels():
    assert count_vowels('aeiou') == 5
    assert count_vowels('AEIOU') == 5

def test_no_vowels():
    assert count_vowels('bcdfg') == 0

def test_mixed_case():
    assert count_vowels('Hello World') == 3  # В строке "Hello World" гласные: e, o, o
    assert count_vowels('PyThOn') == 1       # В строке "PyThOn" одна гласная: O

import pytest

@pytest.mark.parametrize("test_input, expected", [
    ('aeiou', 5),
    ('bcdfg', 0),
    ('Hello World', 3),
    ('PyThOn', 1),
    ('AEIOU', 5)
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected

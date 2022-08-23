from plates import is_valid

def main():
    test_characters()
    test_two_letters()
    test_numbers_in_the_middle()
    test_first_number_is_zero()
    test_existing_characters()

# Maximum of characters is 6 is while the minimum of characters is 2
def test_characters():
    assert is_valid('AC') == True
    assert is_valid('ACDEFG') == True
    assert is_valid('C') == False
    assert is_valid('ABCDEFGHJKLMINOP') == False

# The plate must start with two letters
def test_two_letters():
    assert is_valid('BB') == True
    assert is_valid('B3') == False
    assert is_valid('33') == False

# No numbers are allowed in the middle of the plate
def test_numbers_in_the_middle():
    assert is_valid('BBB333') == True
    assert is_valid('BBB33B') == False

# The first number can't start out with a 0
def test_first_number_is_zero():
    assert is_valid('CS04') == False
    assert is_valid('CS50') == True
    assert is_valid('CS50R') == False

# Periods, punctuation marks, and no spaces are foridden
def test_existing_characters():
    assert is_valid('SI4.1354') == False
    assert is_valid('CP 40') == False
    assert is_valid('Hi!') == False
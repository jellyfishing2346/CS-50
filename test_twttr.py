from twttr import shorten

def main():
    # Call the following test functions
    test_letter_cases()
    test_numbers()
    test_punctuation()

# Test the vowels for upper case and lower case
def test_letter_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

# Test the case for numbers
def test_numbers():
    assert shorten('1234') == '1234'

# Test the punctuation
def test_punctuation():
    assert shorten('!?.,') == '!?.,'

    if __name__ == "__main__":
        main()
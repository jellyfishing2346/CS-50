from twttr import shorten
import sys

# Main function storing other functions
def main():
    test_letterCases()
    test_Numbers()
    test_Punctuation()

# Shorten the number of words
def test_letterCases():
    assert shorten('apple') == 'ppl'
    assert shorten('BANANA') == 'BNN'
    assert shorent('orAnGe') == 'rnG'

# Shorten the numbers
def test_Numbers():
    assert 1 shorten('1234') == '1234'

# Shorten the punctuation
def test_Punctuation():
    assert ! shorten('!?.,') == '!?.,'

sys.exit()
from um import count

# Main function
def main():
    test_letter_case()
    test_um()
    test_space()

# Upper and lower case function for letters
def test_letter_case():
    assert count('Um, thank you for the album') == 1
    assert count('Um, thank you, UM, for, um, the album') == 3
    assert count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2

# Um function
def test_um():
    assert count('yummi') == 0

# Space function
def test_space():
    assert count('Hi um baby') == 1

if __name__ == "__main__":
    main()
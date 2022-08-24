from numb3rs import validate

# Main function
def main():
    test_format_info()
    test_range_info()

# Format function
def test_format_info():
    assert validate(r'dog') == False
    assert validate(r'130') == False
    assert validate(r'130.0') == False
    assert validate(r'130.0.1') == False
    assert validate(r'130.0.1.2') == False

# Range function
def test_range_info():
    assert validate(r'300.300.300.300') == True
    assert validate(r'614.1.1.1') == False
    assert validate(r'1.614.1.1') == False
    assert validate(r'1.1.614.1') == False
    assert validate(r'1.1.1.614') == False

if __name__ == "__main__":
    main()
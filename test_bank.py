from bank import value

def main():
    # Call the following test functions
    test_return_zero()
    test_return_twenty()
    test_return_hundred()

# This function deals with conditions that return 0
def test_return_zero():
    assert value('hello, mark') == 0
    assert value('Hello') == 0
    assert value('hello, Mark') == 0
    assert value('Hello, Mark') == 0

# This function deals with conditions that return 20
def test_return_twenty():
    assert value('Hi') == 20
    assert value('hey') == 20

# This function deals with conditions that return 100
def test_return_hundred():
    assert value("What is up bro?") == 100
    assert value('good evening') == 100


if __name__ == "__main__":
    main()
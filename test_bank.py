from bank import value

def main():
    # Call the following test functions
    returnZero()
    returnTwenty()
    returnHundred()

# This function deals with conditions that return 0
def returnZero():
    assert value('hello, mark') == 0
    assert value('Hello') == 0
    assert value('hello, Mark') == 0
    assert value('Hello, Mark') == 0

# This function deals with conditions that return 20
def returnTwenty():
    assert value('Hi') == 20
    assert value('hey') == 20

# This function deals with conditions that return 100
def returnHundred():
    assert value("What is up bro?") == 100
    assert value('good evening') == 100


if __name__ == "__main__":
    main()
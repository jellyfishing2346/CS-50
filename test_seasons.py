from seasons import check_birthday_info

# Main function
def main():
    test_check_birthday_info()

# This function is to verify a person's birthday info
def test_check_birthday_info():
    assert check_birthday_info("July 3, 1998") == None
    assert check_birthday_info("1998-7-3") == None
    assert check_birthday_info("1998-07-03") == ("1998", "07", "03")

if __name__ == "__main__":
    main()
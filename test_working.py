from working import convert
import pytest

# Main function
def main():
    test_wrong_format_info()
    test_time_format_info()
    test_wrong_hour_info()
    test_wrong_minute_info()
    test_invalid_time_format()

# Check for ValueError
def test_wrong_format_info():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

# Time format function
def test_time_format_info():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'

# Check if the hour is wrong
def test_wrong_hour_info():
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00')

# Check if the minutes are wrong
def test_wrong_minute_info():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

# Invalid time format
def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
        convert('9 AM : 5 PM')
        convert('9 AM // 5 PM')
        convert('9 AM ---- 5 PM')
        convert('9 AM <-> 5 PM')
        convert('9 AM - 5 PM')
        convert('10:7 AM // 5:1 PM')

if __name__ == "__main__":
    main()
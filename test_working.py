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
        convert('9 AM:12 - 5 PM:14')
        convert('9 AM : 5 PM')
        convert('9 AM // 5 PM')
        convert('9 AM ---- 5 PM')
        convert('9 AM <-> 5 PM')
        convert('9 AM - 5 PM')
        convert('10:7 AM - 5:1 PM')
        convert('10::7 AM - 5::1 PM')
        convert('10:12:05 AM - 17:10:01 PM')
        convert('1212 to 1111')
        convert('1212 AM to 1111 PM')
        convert('9 to 5')
        convert('8@00 PM to 8@00 AM')
        convert('8-00 PM to 8-00 AM')
        convert('8/00 PM to 8/00 AM')
        convert('8 00 PM to 8 00 AM')
        convert('15:15 to 17:10')
        convert('9:0 AM to 5:0 PM')
        convert('9:0 AM to 5:01 PM')
        convert('9:01 AM to 5:0 PM')
        convert('9:0 AM to 5:0 PM')
        convert('@@:ER to YR:##')
        convert('9:01 BM to 5:01 PM')
        convert('9:01 AM to 5:01 BM')
        convert('9:01 BM to 5:01 BM')
        convert('9:01 CM to 5:01 PM')
        convert('9:01 AM to 5:01 CM')
        convert('9:01 CM to 5:01 CM')
        convert('9:01 DM to 5:01 PM')
        convert('9:01 AM to 5:01 DM')
        convert('9:01 DM to 5:01 DM')
        convert('9:01 EM to 5:01 PM')
        convert('9:01 AM to 5:01 EM')
        convert('9:01 EM to 5:01 EM')
        convert('9:01 FM to 5:01 PM')
        convert('9:01 AM to 5:01 FM')
        convert('9:01 FM to 5:01 FM')
        convert('9:01 GM to 5:01 PM')
        convert('9:01 AM to 5:01 GM')
        convert('9:01 GM to 5:01 GM')
        convert('9:01 HM to 5:01 PM')
        convert('9:01 AM to 5:01 HM')
        convert('9:01 HM to 5:01 HM')
        convert('9:01 JM to 5:01 PM')
        convert('9:01 AM to 5:01 JM')
        convert('9:01 JM to 5:01 JM')
        convert('9:01 KM to 5:01 PM')
        convert('9:01 AM to 5:01 KM')
        convert('9:01 KM to 5:01 KM')
        convert('9:01 LM to 5:01 PM')
        convert('9:01 AM to 5:01 LM')
        convert('9:01 LM to 5:01 LM')
        convert('9:01 MM to 5:01 PM')
        convert('9:01 AM to 5:01 MM')
        convert('9:01 MM to 5:01 MM')
        convert('9:01 NM to 5:01 PM')
        convert('9:01 AM to 5:01 NM')
        convert('9:01 NM to 5:01 NM')
        convert('9:01 OM to 5:01 PM')
        convert('9:01 AM to 5:01 OM')
        convert('9:01 OM to 5:01 OM')
        convert('9:01 QM to 5:01 PM')
        convert('9:01 AM to 5:01 QM')
        convert('9:01 QM to 5:01 QM')
        convert('9:01 RM to 5:01 PM')
        convert('9:01 AM to 5:01 RM')
        convert('9:01 RM to 5:01 RM')
        convert('9:01 SM to 5:01 PM')
        convert('9:01 AM to 5:01 SM')
        convert('9:01 SM to 5:01 SM')
        convert('9:01 TM to 5:01 PM')
        convert('9:01 AM to 5:01 TM')
        convert('9:01 TM to 5:01 TM')
        convert('9:01 UM to 5:01 PM')
        convert('9:01 AM to 5:01 UM')
        convert('9:01 UM to 5:01 UM')
        convert('9:01 VM to 5:01 PM')
        convert('9:01 AM to 5:01 VM')
        convert('9:01 VM to 5:01 VM')
        convert('9:01 WM to 5:01 PM')
        convert('9:01 AM to 5:01 WM')
        convert('9:01 WM to 5:01 WM')
        convert('9:01 XM to 5:01 PM')
        convert('9:01 AM to 5:01 XM')
        convert('9:01 XM to 5:01 XM')
        convert('9:01 YM to 5:01 PM')
        convert('9:01 AM to 5:01 YM')
        convert('9:01 YM to 5:01 YM')
        convert('9:01 ZM to 5:01 PM')
        convert('9:01 AM to 5:01 ZM')
        convert('9:01 ZM to 5:01 ZM')


if __name__ == "__main__":
    main()
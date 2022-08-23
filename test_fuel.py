from fuel import convert, gauge
import pytest

def main():
    test_zero_divison_result()
    test_for_value_error()
    test_for_correct_output()

def test_zero_divison_result():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_for_value_error():
    with pytest.raises(ValueError):
        convert('monkey/chimpanzee')

def test_for_correct_output():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

if __name__ == "__main__":
    main()
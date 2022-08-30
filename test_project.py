from project import check_correct_argument_info, select_character, select_age
import pytest

def test_check_correct_argument_info():
    with pytest.raises(SystemExit):
        check_correct_argument_info()


def test_select_character():
    assert select_character("funny") == "Class Clown"
    assert select_character("quirky") == "Class Clown"
    assert select_character("buffon") == "Class Clown"
    assert select_character("gullible") == "UnInterested"
    assert select_character("emo") == "UnInterested"
    assert select_character("dull") == "UnInterested"
    assert select_character("angry") == "Unlikeable"
    assert select_character("annoying") == "Unlikeable"
    assert select_character("arrognant") == "Unlikeable"
    assert select_character("mischievous") == "Untolerable"

def test_select_age():
    assert select_age(1978) ==  "Age 44"
    assert select_age(1979) ==  "Age 43"
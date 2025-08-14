from lib.age_verification import *
import pytest 

# raise exception if input is empty 
def test_raise_exception_if_input_empty(): 
    with pytest.raises(Exception) as e: 
        age_verification("") 
    assert str(e.value) == "Please enter your date of birth"

def test_raise_exception_if_input_incorrect_format():
    with pytest.raises(Exception) as e:
        age_verification("12-12-12")
    assert str(e.value) == "Please enter your date of birth in YYYY-MM-DD format"

def test_if_age_is_correct_and_over_16(): 
    assert age_verification("2009-01-01") == "Access granted"
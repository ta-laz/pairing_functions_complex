from lib.age_verification import *
import pytest 

# raise exception if input is empty 
def test_raise_exception_if_input_empty(): 
    with pytest.raises(Exception) as e: 
        age_verification("") 
    assert str(e.value) == "Please enter your date of birth"
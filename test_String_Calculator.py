from String_Calculator import Add
import pytest

def test_adding_empty_string():
    result = 0
    assert Add('') == result

def test_add_one_number():
    result = 1
    assert Add('1') == result
    result = 10
    assert Add('10') == result
            
def test_add_two_numbers():
    result = 3
    assert Add('1,2') == result
    result = 55
    assert Add('50,5') == result

def test_add_multiple_numbers():
    result = 11
    assert Add('1,2,8') == result
    result = 60
    assert Add('50,5,5') == result

def test_add_with_new_line():
    result = 6
    assert Add('1\n2,3') == result

def test_add_diff_delimiter2():
    result = 3
    assert Add('//;\n1;2') == result
    result = 20
    assert Add('//;\n18;2') == result

def test_add_negative():
     with pytest.raises(Exception):
        result = Exception(f'this -1 is a negative')
        assert Add('-1') == result

def test_multiple_negatives():
    with pytest.raises(Exception):
        result = Exception(f'this -1 is a negative')
        assert Add('-1,2,-3') == result
        result = Exception(f'this -1 is a negative')
        assert Add('-1,//;\n-18;2') == result
        result = Exception(f'this -1 is a negative')
        assert Add('-1') == result


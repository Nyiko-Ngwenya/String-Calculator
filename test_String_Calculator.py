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
        result = Exception('this [-1] is a negative ,negatives not allowed')
        assert Add('-1') == result

def test_multiple_negatives():
    with pytest.raises(Exception):
        result = Exception('these  [-1,-3] are negative')
        assert Add('-1,2,-3') == result
        result = Exception('these  [-1,-18] are negative')
        assert Add('-1,//;\n-18;2') == result
        result = Exception('these [-1,-2,-3,-4] are negative')
        assert Add('-1,-2,-3,-4') == result

def test_adding_big_numbers():
    result = 2
    assert Add('1000,2') == 2

def test_long_delimiters():
    result = 6
    assert Add('//[***]\n1***2***3') == result

def test_multiple_delimiters():
    result = 6
    assert Add('//[*][%]\n1*2%3') == result

def test_letters_fail():
    result = 0
    assert Add('abc') == result
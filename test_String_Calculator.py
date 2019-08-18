from String_Calculator import Add

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

def test_add_diff_delimiters():
    result = 3
    assert Add('//;\n1;2') == result
    result = 20
    assert Add('//;\n18;2') == result

def test_add_negative():
    result = 3
    assert Add('//;\n1;2') == result
    result = 20
    assert Add('//;\n18;2') == result

def test_except_diff_delimiters():
    result = 3
    assert Add('//;\n1;2') == result
    result = 20
    assert Add('//;\n18;2') == result
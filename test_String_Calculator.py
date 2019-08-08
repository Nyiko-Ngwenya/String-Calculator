from String_Calculator import addition,addition2,addition_proper

def test_addition():
    assert addition('','') == 0
    assert addition('3','3') == 6
    assert addition('','3') == 3
    #assert addition('3', '3','3') == 9
    #assert addition('3', '3','3','3') == 12
    
def test_addition2():
    assert addition2('','') == 0
    assert addition2('3','3') == 6
    assert addition2('','3') == 3
    assert addition2('3', '3','3') == 9
    assert addition2('3', '3','3','3') == 12
    assert addition2('3', '3','3','3') == 12
    #assert addition2('1\n2,3') == 6

def test_addition_proper():
    assert addition_proper('1,2') == 3
    assert addition_proper('10,2,5,5') == 22
    assert addition_proper('5,2') == 7
    assert addition_proper('') == 0
    assert addition2('1\n2,3') == 6
    assert addition2('10\n5,5') == 20

            
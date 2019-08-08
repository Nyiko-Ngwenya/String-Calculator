from String_Calculator import addition,addition2

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
            
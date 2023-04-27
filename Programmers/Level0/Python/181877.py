# 181877 대문자로 바꾸기

def solution(myString):
    return myString.upper()

def test_sample():
    assert solution("aBcDeFg") == "ABCDEFG"
    assert solution("AAA") == "AAA"


test_sample()

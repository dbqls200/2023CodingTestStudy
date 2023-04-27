# 181876 소문자로 바꾸기

def solution(myString):
    return myString.lower()

def test_sample():
    assert solution("aBcDeFg") == "abcdefg"
    assert solution("aaa") == "aaa"

test_sample()

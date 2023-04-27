# 181869 공백으로 구분하기 1

def solution(my_string):
    return my_string.split()

def test_sample():
    assert solution("i love you") == ["i", "love", "you"]
    assert solution("programmers") == ["programmers"]


test_sample()

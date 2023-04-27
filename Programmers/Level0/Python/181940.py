# 181940 문자열 곱하기

def solution(my_string, k):
    return my_string * k

def test_sample():
    assert solution('string', 3) == "stringstringstring"
    assert solution('love', 10) == "lovelovelovelovelovelovelovelovelovelove"

test_sample()

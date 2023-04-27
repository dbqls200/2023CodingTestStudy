# 181849 문자열 정수의 합

def solution(num_str):
    return sum(map(int, num_str))

def test_sample():
    assert solution("123456789") == 45
    assert solution("1000000") == 1

test_sample()

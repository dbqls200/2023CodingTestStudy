# 181843 부분 문자열인지 확인하기

def solution(my_string, target):
    return 1 if target in my_string else 0

def test_sample():
    assert solution("banana", "ana") == 1
    assert solution("banana", "wxyz") == 0

test_sample()

# 181933 flag에 따라 다른 값 반환하기

def solution(a, b, flag):
    return a + b if flag else a - b

def test_sample():
    assert solution(-4, 7, True) == 3
    assert solution(-4, 7, False) == -11

test_sample()

# 181939 더 크게 합치기

def solution(a, b):
    a, b = str(a), str(b)
    return max(int(a + b), int(b + a))

def test_sample():
    assert solution(9, 91) == 991
    assert solution(89, 8) == 898

test_sample()

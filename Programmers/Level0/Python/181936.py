# 181936 공배수

def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0

def test_sample():
    assert solution(60, 2, 3) == 1
    assert solution(55, 10, 5) == 0

test_sample()

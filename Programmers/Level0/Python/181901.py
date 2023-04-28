# 181901 배열 만들기 1

def solution(n, k):
    return [i for i in range(k, n + 1, k)]

def test_sample():
    assert solution(10, 3) == [3, 6, 9]
    assert solution(15, 5) == [5, 10, 15]

test_sample()

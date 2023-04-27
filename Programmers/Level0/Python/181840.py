# 181840 정수 찾기

def solution(num_list, n):
    return 1 if n in num_list else 0

def test_sample():
    assert solution([1, 2, 3, 4, 5], 3) == 1
    assert solution([15, 98, 23, 2, 15], 20) == 0


test_sample()

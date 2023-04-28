# 181892 n 번째 원소부터

def solution(num_list, n):
    return num_list[n - 1:]

def test_sample():
    assert solution([2, 1, 6], 3) == [6]
    assert solution([5, 2, 1, 7, 5], 2) == [2, 1, 7, 5]

test_sample()

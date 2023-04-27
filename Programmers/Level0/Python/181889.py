# 181889 n 번째 원소까지

def solution(num_list, n):
    return num_list[:n]

def test_sample():
    assert solution([2, 1, 6], 1) == [2]
    assert solution([5, 2, 1, 7, 5], 3) == [5, 2, 1]


test_sample()

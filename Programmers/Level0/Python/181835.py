# 181835 조건에 맞게 수열 변환하기 3

def solution(arr, k):
    if k % 2 != 0:
        return [a * k for a in arr]
    else:
        return [a + k for a in arr]

def test_sample():
    assert solution([1, 2, 3, 100, 99, 98], 3) == [3, 6, 9, 300, 297, 294]
    assert solution([1, 2, 3, 100, 99, 98], 2) == [3, 4, 5, 102, 101, 100] 

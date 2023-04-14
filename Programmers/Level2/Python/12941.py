# 12941 최솟값 만들기

def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum([A[i] * B[i] for i in range(len(A))])

def solution2(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

def test_sample():
    assert solution([1, 4, 2], [5, 4, 4]) == 29
    assert solution([1,2], [3,4]) == 10

    assert solution2([1, 4, 2], [5, 4, 4]) == 29
    assert solution2([1,2], [3,4]) == 10

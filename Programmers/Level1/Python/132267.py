# 132267 콜라 문제

def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += ((n // a) * b)
        n = (n % a) + ((n // a) * b)

    return answer

def test_sample():
    assert solution(2, 1, 20) == 19
    assert solution(3, 1, 20) == 9

test_sample()

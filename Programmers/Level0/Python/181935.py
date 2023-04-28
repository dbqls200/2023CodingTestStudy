# 181935 홀짝에 따라 다른 값 반환하기

def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(1, n + 1, 2):
            answer += i
    else:
        for i in range(2, n + 1, 2):
            answer += (i * i)
    return answer


def test_sample():
    assert solution(7) == 16
    assert solution(10) == 220


test_sample()

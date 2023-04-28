# 181884 n보다 커질 때까지 더하기


def solution(numbers, n):
    answer = 0
    for num in numbers:
        if answer > n:
            return answer
        else:
            answer += num 
    return answer


def test_sample():
    assert solution([34, 5, 71, 29, 100, 34], 123) == 139
    assert solution([58, 44, 27, 10, 100], 139) == 239

test_sample()

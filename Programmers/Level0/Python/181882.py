# 181882 조건에 맞게 수열 변환하기 1


def solution(arr):
    answer = []
    for a in arr:
        if a % 2 != 0 and a < 50:
            answer.append(a * 2)
        elif a % 2 == 0 and a >= 50:
            answer.append(a // 2)
        else:
            answer.append(a)
    return answer

def test_sample():
    assert solution([1, 2, 3, 100, 99, 98]) == [2, 2, 6, 50, 99, 49]

test_sample()

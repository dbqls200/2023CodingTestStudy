# 134240 푸드 파이트 대회

def solution(food):
    answer = ''

    for i in range(1, len(food)):
        answer += (str(i) * (food[i] // 2))

    temp = ''.join(sorted(answer)[::-1])

    return answer + '0' + temp


def test_sample():
    assert solution([1, 3, 4, 6]) == "1223330333221"
    assert solution([1, 7, 1, 2]) == "111303111"


test_sample()

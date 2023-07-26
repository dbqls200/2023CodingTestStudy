# P.96 숫자 카드 게임

# 1. 각 행마다 가장 작은 수를 고르고
# 2. 그 중에서 가장 큰 수 선택하기

def solution(n, m, array):
    answer = 0
    
    for arr in array:
        answer = max(min(arr), answer)

    return answer

def test_sample():
    assert solution(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]) == 2
    assert solution(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]) == 3

test_sample()


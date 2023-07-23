# 5585 거스름돈
# Bronze2

# 그리디 알고리즘
# 금액이 큰 동전부터 거슬러주면 가장 적은 동전 갯수로 거슬러줄 수 있다.


def solution(n):
    n = 1000 - n
    answer = 0
    coins = [500, 100, 50, 10, 5, 1]

    for coin in coins:
        answer += (n // coin)
        n %= coin

    return answer


def test_sample():
    assert solution(380) == 4
    assert solution(1) == 15


test_sample()

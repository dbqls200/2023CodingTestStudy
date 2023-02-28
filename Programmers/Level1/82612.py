# 82612 부족한 금액 계산하기

def solution(price, money, count):
    answer = sum(price * i for i in range(1, count + 1))
    return answer-money if answer-money > 0 else 0

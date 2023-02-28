# 120891 369게임

def solution(order):
    answer = 0
    for i in list(str(order)):
        if int(i) in [3, 6, 9]:
            answer += 1

    return answer

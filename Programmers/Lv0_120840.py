# 120840 구슬을 나누는 경우의 수

from itertools import combinations

def solution(balls, share):
    temp = [i for i in range(balls)]
    comb = list(combinations(temp, share))
    return len(comb)

def solution2(balls, share):
    return factorial(balls) // (factorial(balls-share) * factorial(share))

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

print(solution(3, 2))
print(solution2(3, 2))

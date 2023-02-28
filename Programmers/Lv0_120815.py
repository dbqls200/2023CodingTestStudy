# 120815 피자 나눠 먹기 (2)

import math

def solution(n):
    return math.lcm(6, n) // 6

print(solution(10))

# 위 방법은 Nope.
# 프로그래머스 파이썬 버전은 3.8.5
# math의 lcm 함수는 3.9 버전 이후로 사용 가능

import math

def solution(n):
    return ((6 * n) // math.gcd(6, n)) // 6

print(solution(10))

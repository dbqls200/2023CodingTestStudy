# 12940 최대공약수와 최소공배수

import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append((n * m) // answer[0])
    return answer

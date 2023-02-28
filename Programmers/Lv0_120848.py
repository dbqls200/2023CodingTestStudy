# 120848 팩토리얼

from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1

    return k

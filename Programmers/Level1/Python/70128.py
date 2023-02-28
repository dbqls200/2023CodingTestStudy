# 70128 내적

def solution(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

def solution2(a, b):
    return sum(x * y for x, y in zip(a, b))

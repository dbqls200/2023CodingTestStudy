# 12912 두 정수 사이의 합

def solution(a, b):
    if a == b:
        return a
    return sum(range(min(a, b), max(a, b)+1))

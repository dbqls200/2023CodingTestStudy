# 12915 문자열 내 마음대로 정렬하기

def solution(strings, n):
    strings.sort()
    return sorted(strings, key = lambda x: x[n])

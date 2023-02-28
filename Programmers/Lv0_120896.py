# 120896 한 번만 등장한 문자

def solution(s):
    return ''.join(sorted(ch for ch in s if s.count(ch) == 1))

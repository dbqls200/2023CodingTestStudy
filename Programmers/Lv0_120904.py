# 120904 숫자 찾기

def solution(num, k):
    num = list(str(num))
    return -1 if str(k) not in num else num.index(str(k))+1

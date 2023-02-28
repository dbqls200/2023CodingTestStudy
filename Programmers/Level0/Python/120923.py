# 120923 연속된 수의 합

def solution(num, total):
    mid = total // num
    return [i for i in range(mid - (num-1)//2, mid + (mid+2)//2)]

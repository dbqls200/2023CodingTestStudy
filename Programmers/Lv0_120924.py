# 120924 다음에 올 숫자

def solution(common):
    temp = common[1] - common[0]
    if common[1] + temp == common[2]:
        return common[-1] + temp
    else:
        temp = common[1] // common[0]
        return common[-1] * temp

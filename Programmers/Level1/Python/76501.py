# 76501 음양 더하기

def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))

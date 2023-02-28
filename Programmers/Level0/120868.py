# 120868 삼각형의 완성조건 (2)

def solution(sides):
    sides.sort()
    return len([i for i in range(max(sides)-min(sides)+1, sum(sides))])

def solution2(sides):
    return sum(sides) - max(sides) + min(sides) + 1

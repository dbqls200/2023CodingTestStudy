# 181839 주사위 게임 1

def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return a * a + b * b
    elif a % 2 != 0 or b % 2 != 0:
        return 2 * (a + b)
    else:
        return abs(a - b)

def test_sample():
    assert solution(3, 5) == 34
    assert solution(6, 1) == 14
    assert solution(2, 4) == 2

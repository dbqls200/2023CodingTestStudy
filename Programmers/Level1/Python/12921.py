# 12921 소수 찾기

def solution1(n):
    cnt = 0
    check = [False, False] + [True] * (n - 1)
    
    for i in range(2, n + 1):
        if check[i]:
            cnt += 1
            for j in range(2 * i, n + 1, i):
                check[j] = False

    return cnt

def solution2(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
            
    return len(num)


def test_sample():
    assert solution1(10) == 4
    assert solution1(5) == 3

    assert solution2(10) == 4
    assert solution2(5) == 3

test_sample()

# 12911 다음 큰 숫자

def solution(n):
    n_count = bin(n).count('1')

    while True:
        n += 1
        
        if n_count == bin(n).count('1'):
            return n

def test_solution():
    assert solution(78) == 83
    assert solution(15) == 23


test_solution()

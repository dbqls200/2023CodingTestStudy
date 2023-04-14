# 12977 소수 만들기

from itertools import combinations

def solution(nums):
    answer = 0

    # 조합 경우의 수 만들기.
    # sum으로 나온 값이 소수인지 판단해서 cnt 올리기
    # 가장 큰 3개 수 더해서 그 수까지 소수 구해놓기.
    
    comb_list = list(combinations(nums, 3))
    comb_sum_list = [sum(n) for n in comb_list]
    n = max(comb_sum_list)
    prime_nums = set(range(2, n + 1))
    
    for i in range(2, n + 1):
        if i in prime_nums:
            prime_nums -= set(range(2 * i, n + 1, i))
            
    for n in comb_sum_list:
        if n in prime_nums:
            answer += 1
    
    return answer

def test_sample():
    assert solution([1, 2, 3, 4]) == 1
    assert solution([1, 2, 7, 6, 4]) == 4


test_sample()

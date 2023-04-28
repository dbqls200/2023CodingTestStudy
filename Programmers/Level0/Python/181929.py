# 181929 원소들의 곱과 합

def solution(num_list):
    hap = sum(num_list)
    gop = 1

    for num in num_list:
        gop *= num

    if hap * hap > gop: return 1
    else: return 0

def test_sample():
    assert solution([3, 4, 5, 2, 1]) == 1
    assert solution([5, 7, 8, 3]) == 0

test_sample()

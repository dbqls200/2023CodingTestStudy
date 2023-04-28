# 181928 이어 붙인 수

def solution(num_list):
    odd = ''
    even = ''
    for num in num_list:
        if num % 2 != 0:
            odd += str(num)
        else:
            even += str(num)
    return int(odd) + int(even)

def test_sample():
    assert solution([3, 4, 5, 2, 1]) == 393
    assert solution([5, 7, 8, 3]) == 581

test_sample()

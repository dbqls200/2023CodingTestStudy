# 181896 첫 번째로 나오는 음수

def solution(num_list):
    for num in num_list:
        if num < 0:
            return num_list.index(num)
        
    return -1

def test_sample():
    assert solution([12, 4, 15, 46, 38, -2, 15]) == 5
    assert solution([13, 22, 53, 24, 15, 6]) == -1

test_sample()

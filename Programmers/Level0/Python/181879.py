# 181879 길이에 따른 연산

def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for num in num_list:
            answer *= num
            
    return answer


def test_sample():
    assert solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]) == 51
    assert solution([2, 3, 4, 5]) == 120

test_sample()

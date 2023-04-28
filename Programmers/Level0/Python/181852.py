# 181852 뒤에서 5등 위로

def solution(num_list):
    return sorted(num_list)[5:]


def test_sample():
    assert solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]) == [15, 32, 38, 46, 56]

test_sample()

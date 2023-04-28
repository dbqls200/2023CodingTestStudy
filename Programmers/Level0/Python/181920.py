# 181920 카운트 업

def solution(start, end):
    return [i for i in range(start, end + 1)]

def test_sample():
    assert solution(3, 10) == [3, 4, 5, 6, 7, 8, 9, 10]

test_sample()

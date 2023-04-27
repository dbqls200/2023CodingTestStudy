# 181899 카운트 다운

def solution(start, end):
    return [i for i in range(start, end - 1, -1)]

def test_sample():
    assert solution(10, 3) == [10, 9, 8, 7, 6, 5, 4, 3]

test_sample()

# 12939 최댓값과 최솟값

def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + ' ' + str(max(s))

def test_sample():
    assert solution("1 2 3 4") == "1 4"
    assert solution("-1 -2 -3 -4") == "-4 -1"
    assert solution("-1 -1") == "-1 -1"

test_sample()

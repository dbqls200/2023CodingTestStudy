# 181842 부분 문자열

def solution(str1, str2):
    return 1 if str1 in str2 else 0

def test_sample():
    assert solution("abc", "aabcc") == 1
    assert solution("tbt", "tbbttb") == 0

test_sample()

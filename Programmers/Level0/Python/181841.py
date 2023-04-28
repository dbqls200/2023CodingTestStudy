# 181841 꼬리 문자열

def solution(str_list, ex):
    return ''.join([string for string in str_list if not ex in string])

def test_sample():
    assert solution(["abc", "def", "ghi"],"ef") == "abcghi"
    assert solution(["abc", "bbc", "cbc"], "c") == ""

test_sample()

# 181915 글자 이어 붙여 문자열 만들기

def solution(my_string, index_list):
    answer = ''

    for index in index_list:
        answer += my_string[index]

    return answer

def test_sample():
    assert solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]) == "programmers"
    assert solution("zpiaz", [1, 2, 0, 0, 3]) == "pizza"


test_sample()

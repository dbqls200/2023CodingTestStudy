# 12951 JadenCase 문자열 만들기

import string

def solution(s):
    return string.capwords(s, sep=' ')

def solution2(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])

def test_solution():
    assert solution("3people unFollowed me") == "3people Unfollowed Me"
    assert solution("for the last week") == "For The Last Week"

    assert solution2("3people unFollowed me") == "3people Unfollowed Me"
    assert solution2("for the last week") == "For The Last Week"


test_solution()


# 181907 문자열의 앞의 n 글자

def solution(my_string, n):
    return my_string[:n]

def test_sample():
    assert solution("ProgrammerS123", 11) == "ProgrammerS"
    assert solution("He110W0r1d", 5) == "He110"


test_sample()

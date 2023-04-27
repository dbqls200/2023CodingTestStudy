# 181910 문자열의 뒤의 n글자

def solution(my_string, n):
    return my_string[-n:]

def test_sample():
    assert solution("ProgrammerS123", 11) == "grammserS123"
    assert solution("He110W0r1d", 5) == "W0r1d"

print(solution("ProgrammerS123", 11))

test_sample()


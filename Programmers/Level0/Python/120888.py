# 120888 중복된 문자 제거

def solution(my_string):
    answer = ''
    for s in my_string:
        if s not in answer:
            answer += s
    return answer

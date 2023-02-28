# 120834 외계행성의 나이

def solution(age):
    answer = ''
    age = list(str(age))
    alpha = list('abcdefghij')
    for a in age:
        answer += alpha[int(a)]
    return answer

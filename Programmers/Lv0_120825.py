# 120825 문자 반복 출력하기

def solution(my_string, n):
    return ''.join([i * n for i in my_string])

print(solution('hello', 3))

# 120864 숨어있는 숫자의 덧셈 (2)

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

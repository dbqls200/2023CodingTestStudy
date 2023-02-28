# 120902 문자열 계산하기

def solution(my_string):
    return eval(my_string)

def solution2(my_string):
    return sum(int(s) for s in my_string.replace('-', '+ -').split('+'))

# 120850 문자열 정렬하기 (1)

def solution(my_string):
    return sorted(list([int(i) for i in my_string if i.isdigit()])

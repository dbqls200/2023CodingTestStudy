# 120826 특정 문자 제거하기

def solution(my_string, letter):
    return ''.join(str for str in my_string if str != letter)

# 120849 모음 제거

def solution(my_string):
    return ''.join([str for str in my_string if str not in ['a', 'e', 'i', 'o', 'u']])

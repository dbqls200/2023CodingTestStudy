# 12916 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    p = s.count('p')
    y = s.count('y')


    if p == y and p != 0:
        return True
    else:
        return False

print(solution('PppYyyeee'))
print(solution('dad'))

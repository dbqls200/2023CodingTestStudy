# 120853 컨트롤 제트

def solution(s):
    s = s.split()
    answer = 0
    for i in range(len(s)):
        if s[i] == 'Z':
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    return answer

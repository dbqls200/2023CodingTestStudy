# 12933 정수 내림차순으로 배치하기

# 처음 생각한 방식
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    result = int(''.join(n))

    return result

# 참고한 방식
def solution2(n):
    return int(''.join(sorted(str(n), reverse=True))

print(solution(266345435))
print(solution2(266345435))

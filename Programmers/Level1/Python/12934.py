# 12934 정수 제곱근 판별

import math

# 처음 생각한 방식 
def solution(n):
    sqrt = math.sqrt(n)

    if int(sqrt) == sqrt:
        return pow(sqrt + 1, 2)
    else:
        return -1

print(solution(121))
print(solution(3))


# 참고한 방식
def solution2(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2

    return -1

print(solution2(121))
print(solution2(3))

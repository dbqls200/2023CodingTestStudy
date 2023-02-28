# 12928 약수의 합

# 처음 생각한 방식 
def solution(num):
    result = 0
    result += num

    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            result += i

    return result

print(solution(12))

# 참고한 방식
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

print(sumDivisor(12))

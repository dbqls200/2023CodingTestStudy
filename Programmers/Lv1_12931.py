# 12931 자릿수 더하기

result = 0

# 처음 생각한 방식 
def solution(num):
    result = 0
    n = len(str(num))
    digit = 10 ** (n - 1)

    for _ in range(n):
        result += num // digit
        num = num % digit
        digit = digit // 10

    return result

print(solution(123))
print(solution(987))


# 새로 알게된 방식
def solution2(num):
    temp = list(map(int, list(str(num))))
    result = sum(temp)

    return result

print(solution2(123))


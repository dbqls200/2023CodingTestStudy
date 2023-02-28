# 12947 하샤드 수

def solution(x):
    temp = list(map(int, list(str(x))))
    return True if x % sum(temp) == 0 else False


def solution2(x):
    return x % sum([int(c) for c in str(x)]) == 0

print(solution(10)) # True
print(solution(13)) # false

print(solution2(10)) # True
print(solution2(13)) # False

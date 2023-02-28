# 12944 평균 구하기

def solution(arr):
    return sum(arr) / len(arr)

print(solution([1, 2, 3, 4]))
print(solution([5, 5]))

def solution2(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

print(solution2([1, 2, 3, 4, 5]))
print(solution2([]))

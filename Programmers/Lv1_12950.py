# 12950 행렬의 덧셈

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer

def solution2(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]

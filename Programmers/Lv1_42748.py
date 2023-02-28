# 42748 K번째수

def solution(array, commands):
    answer = []
    temp = []

    for i, j, k in commands:
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])

    return answer

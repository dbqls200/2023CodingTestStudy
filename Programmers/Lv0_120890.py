# 120890 가까운 수

def solution(array, n):
    array = sorted(array)
    result = []
    for i in array:
        result.append(abs(n-i))
    return array[result.index(min(result))]

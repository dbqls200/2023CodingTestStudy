# 12932 자연수 뒤집어 배열로 만들기

# 처음 생각한 방식 
def solution(n):
    arr = list(map(int, list(str(n))))
    arr.reverse()
    return arr

print(solution(12345))

# 참고한 방식
def solution2(n):
    return list(map(int, reversed(str(n))))

print(solution2(12345))


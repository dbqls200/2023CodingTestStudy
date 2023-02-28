# 77884 약수의 개수와 덧셈

def solution(left, right):
    answer = 0

    while left <= right:
        temp = 0

        for i in range(1, left+1):
            if left % i == 0:
                temp += 1

        if temp % 2 == 0:
            answer += left
        else:
            answer -= left

        left += 1

    return answer

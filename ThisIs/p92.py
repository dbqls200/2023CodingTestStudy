# p.92 큰 수의 법칙

# 1. 입력받은 array를 내림차순으로 정렬
# 2. 총 k번 덧셈을 진행하는데 가장 큰 수를 m번, 그 다음 큰 수를 한 번 더해주도록

def solution(n, m, k, array):
    answer = 0
    cnt = 0
    
    array = sorted(array, reverse=True)

    for i in range(m):
        if cnt == k:
            cnt = 0
            answer += array[1]
            continue

        answer += array[0]
        cnt += 1

    return answer

    

def test_sample():
    assert solution(5, 8, 3, [2, 4, 5, 4, 6]) == 46
    assert solution(5, 7, 2, [3, 4, 3, 4, 3]) == 28


test_sample()

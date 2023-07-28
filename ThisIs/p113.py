# p.113 시각

# hour, minute, second 총 3개의 반복문을 돌면서 3이 포함되어 있는지 확인 

def solution(n):
    answer = 0

    for h in range(0, n + 1):
        for m in range(0, 60):
            for s in range(0, 60):
                if '3' in str(h) + str(m) + str(s):
                    answer += 1
    
    return answer
 

def test_sample():
    assert solution(5) == 11475


test_sample()

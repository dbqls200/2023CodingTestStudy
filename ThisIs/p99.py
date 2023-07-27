# p.99 1이 될 때까지

# 1. n이 1 될 때까지 반복문 돌리기
# 2. 반복문 안에서 n이 K로 나누어 떨어지면 k로 나누고
# 3. 아니면 n에서 1 빼기 

def solution(n, k):
    cnt = 0
    
    while True:
        if n == 1:
            break

        if n % k == 0:
            n //= k

        else:
            n -= 1

        cnt += 1

    return cnt

def test_sample():
    assert solution(25, 5) == 2


test_sample()

# 12946 하노이의 탑

# 재귀
# frm : 시작점, to : 도착점, sub : 경유

# 1. 시작점에 있는 n개의 원반 중 n-1개는 sub에 모두 옮겨준다.
# 2. 시작점에 남은 마지막 원반은 도착점 바로 보내준다.
# 3. 경유지에 보낸 n-1개 원반을 도착점으로 보내준다.

def solution(n):
    answer = []
    
    hanoi(n, 1, 3, 2, answer)
    
    return answer

def hanoi(n, frm, to, sub, answer):    
    if n == 1:
        answer.append([frm, to])
        
        return
    
    else:
        hanoi(n - 1, frm, sub, to, answer)
        answer.append([frm, to])
        hanoi(n - 1, sub, to, frm, answer)
        
    return answer


def test_sample():
    assert solution(2) == [[1, 2], [1, 3], [2, 3]]


test_sample()

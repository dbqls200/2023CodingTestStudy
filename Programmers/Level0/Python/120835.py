# 120835 진료순서 정하기

def solution(emergency):
    answer = [0 for _ in range(len(emergency))]
    for i in range(1, len(emergency)+1):
        idx = emergency.index(max(emergency))
        answer[idx] = i
        emergency[idx] = 0

    return answer

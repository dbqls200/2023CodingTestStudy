# 42840 모의고사

def solution(answers):
    answer = []
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    checking = [0] * 3
    
    for i in range(len(answers)):
        if answers[i] == supoja1[i % len(supoja1)]:
            checking[0] += 1
        if answers[i] == supoja2[i % len(supoja2)]:
            checking[1] += 1
        if answers[i] == supoja3[i % len(supoja3)]:
            checking[2] += 1
            
    for i in range(len(checking)):
        if max(checking) == checking[i]:
            answer.append(i + 1)
    
    return answer

def test_sample():
    assert solution([1,2,3,4,5]) == [1]
    assert solution([1,3,2,4,2]) == [1,2,3]

test_sample()

# 42586 기능개발

def solution(progresses, speeds):
    answer = []    
    release = []
    
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        day = remain // s
        
        if remain % s != 0:
            day += 1
        release.append(day)
    
    now = 0
    for i in range(1, len(release)):
        if release[i] > release[now]:
            answer.append(i - now)
            now = i
            
    answer.append(len(progresses) - now)

    return answer


def test_sample():
    assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
    assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]


test_sample()

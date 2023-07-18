# 138477 명예의 전당 (1)

# score 점수를 하나씩 가져옴.
# score[i]와 현재 명.전의 min 값이랑 비교.
# k일차까지는 모든 score[i] 명.전에 올리기.
  
# score[i] > 명.전 min 값 => 명.전에 있는 min 값 삭제 후 score[i] 올리기
# score[i] <= 명.전 min 값 => 아무 변화 x    
# 매일 최하위 점수 발표: 명.전 min 값

def solution(k, score):
    answer = []
    hall_of_fame = []
        
    for s in score:
        if len(hall_of_fame) < k:
            hall_of_fame.append(s)
            
        else:
            if s > min(hall_of_fame):
                hall_of_fame.append(s)
                hall_of_fame.remove(min(hall_of_fame))
        
        answer.append(min(hall_of_fame))
        
    return answer

def test_sample():
    assert solution(3, [10, 100, 20, 150, 1, 100, 200]) == [10, 10, 10, 20, 20, 100, 100]
    assert solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]) == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]


test_sample()

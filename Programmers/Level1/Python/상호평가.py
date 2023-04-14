def solution(score):
    answer = ''
    
    score = list(zip(*score))
    score = [list(n) for n in score]
    
    grade = {9: 'A', 8: 'B', 7: 'C', 6: 'D', 5: 'D',
             4: 'F', 3: 'F', 2: 'F', 1: 'F', 0: 'F'}

    for i in range(len(score)):
        cnt = score[i].count(score[i][i])

        if cnt == 1:
            if score[i][i] == max(score[i]) or score[i][i] == min(score[i]):
                score[i].remove(score[i][i])

        avg = (sum(score[i]) / len(score[i])) // 10
        
        answer += grade[avg]

    return answer


def test_sample():
    assert solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]) == "FBABD"
    assert solution([[50,90],[50,87]]) == "DA"
    assert solution([[70,49,90],[68,50,38],[73,31,100]]) == "CFD"


test_sample()

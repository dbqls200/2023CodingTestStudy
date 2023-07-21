# 159994 카드 뭉치

# goal 글자 하나씩 가져오기
# cards1이나 cards2의 첫번째 원소와 비교해보고
# 있으면 계속 진행
# 없으면 No 반
    
def solution1(cards1, cards2, goal):
    for s in goal:
        if cards1 and s == cards1[0]:
            cards1.pop(0)
            
        elif cards2 and s == cards2[0]:
            cards2.pop(0)
            
        else:
            return "No"
        
    return "Yes"


def test_sample():
    assert solution1(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]) == "Yes"
    assert solution1(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]) == "No"


test_sample()


# 방법 2
# goal을 슬라이싱해서 cards1 또는 cards2에 있는지 확인하기
# 더 확인 필요함.

def solution2(cards1, cards2, goal):
    for i in range(0, len(goal)+1):
        for j in range(i+1, len(goal)+1):
            print(goal[i:j])
            
            if goal[i:j] in cards1:
                print("1", goal[i:j])
                continue
            
            elif goal[i:j] in cards2:
                print("2 : ", goal[i:j])
                continue
            
            
    return "Yes"

# 방법 3
# cards1에 있는 단어를 goal에 몇번째에 있는지 확인
# cards2도 동일.
# 단어가 순서대로 있다면, 인덱스가 정렬되어 있을 것이고
# 그렇지 않으면 정렬되어 있지 않을 것.

# 더 확인이 필요한 방법. 예외사항이 있음.
def solution3(cards1, cards2, goal):
    cards1_index = []
    cards2_index = []
    
    for word in cards1:
        cards1_index.append(goal.index(word))
        
    for word in cards2:
        cards2_index.append(goal.index(word))
    
    if cards1_index == sorted(cards1_index) and cards2_index == sorted(cards2_index):
        return "Yes"
    else:
        return "No"

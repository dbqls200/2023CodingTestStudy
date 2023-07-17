# 176963 추억 점수

def solution(name, yearning, photo):
    answer = []
    pointDict = dict(zip(name, yearning))

    for members in photo:
        point = 0

        for member in members:
            if member in pointDict:
                point += pointDict[member]

        answer.append(point)

    return answer

def test_sample():
    assert solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]) ==  [19, 15, 6]
    assert solution(["kali", "mari", "don"], [11, 1, 55],  [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]) == [67, 0, 55]
    assert solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],  [["may"],["kein", "deny", "may"], ["kon", "coni"]]) == [5, 15, 0]


test_sample()

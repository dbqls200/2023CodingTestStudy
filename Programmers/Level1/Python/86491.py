# 86491 최소직사각형

# 처음 작성한 코드
def solution1(sizes):
    temp = []
    width = 0
    height = 0

    for w, h in sizes:
        if w < h:
            w, h = h, w

        temp.append([w, h])

    width = max(t[0] for t in temp)
    height = max(t[1] for t in temp)

    return width * height

# 참고한 코드
def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


def test_sample():
    assert solution1([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000
    assert solution1([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120
    assert solution1([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133

    assert solution2([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000
    assert solution2([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120
    assert solution2([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133
    
test_sample()

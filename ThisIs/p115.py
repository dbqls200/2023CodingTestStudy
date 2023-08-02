# p.115 왕실의 나이트

def solution(data):
    alpha = {'a': 1,
             'b': 2,
             'c': 3,
             'd': 4,
             'e': 5,
             'f': 6,
             'g': 7,
             'h': 8}
        
    moves = [[-2, -1],
            [-2, 1],
            [2, -1],
            [2, 1],
            [-1, -2],
            [-1, 2],
            [1, -2],
            [1, 2]]

    x, y = alpha[data[0]], int(data[1])
    answer = 0

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]

        if nx > 8 or ny > 8 or nx < 1 or ny < 1:
            continue

        answer += 1

    return answer

def test_sample():
    assert solution('a1') == 2
    assert solution('c2') == 6


test_sample()

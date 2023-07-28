# p.110 상하좌우

# 1.

def solution(n, move):
    x, y = 1, 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for m in move:
        if m == 'L':
            if x + dx[0] < 1 or y + dy[0] < 1:
                continue
            x += dx[0]
            y += dy[0]

        elif m == 'R':
            if x + dx[1] < 1 or y + dy[1] < 1:
                continue
            x += dx[1]
            y += dy[1]

        elif m == 'U':
            if x + dx[2] < 1 or y + dy[2] < 1:
                continue
            x += dx[2]
            y += dy[2]

        elif m == 'D':
            if x + dx[3] < 1 or y + dy[3] < 1:
                continue
            x += dx[3]
            y += dy[3]
        
    return x, y

def solution2(n, moves):
    x, y = 1, 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    types = ['L', 'R', 'U', 'D']

    for move in moves:
        for i in range(len(types)):
            if move == types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue

                x, y = nx, ny

    return x, y

def test_sample():
    assert solution(5, ['R', 'R', 'R', 'U', 'D', 'D']) == (3, 4)
    assert solution2(5, ['R', 'R', 'R', 'U', 'D', 'D']) == (3, 4)


test_sample()

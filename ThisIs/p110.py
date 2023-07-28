# p.110 상하좌우

# 1. moves 길이만큼 반복문 돌리기
# 2. 이동 방향에 맞게 x좌표와 y좌표 조정하기
# 3. 이동했을 때 x, y좌표가 칸을 벗어나면 뛰어넘기


def solution(n, moves):
    x, y = 1, 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for m in moves:
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


# 처음 작성한 solution 코드가 깔끔하지 못한 것 같아서 수정한 버전
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

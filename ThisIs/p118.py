# p118 게임 개발

# 1. 데이터 입력 받기
# 2. 북, 동, 남, 서 방향 설정
# 3. 반복문 돌리기
# 4. 이동할 수 있는 칸일 때
# 5. 이동하지 못 할 때
# 6. 4 방향 모두 회전해도 이동하지 못 할 때
# 7. 왼쪽으로 회전하는 함수

def turn_left():
    global direction
    
    direction += 1

    if direction == 4:
        direction = 0


n, m = map(int, input().split())
x, y, direction = map(int, input().split())

my = [[0] * m for _ in range(n)]

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

move = [[-1, 0], # 북
        [0, -1], # 동
        [1, 0], # 남
        [0, 1]] # 서

my[x][y] = 1    
cnt = 1
turn_time = 0

while True:
    turn_left()

    nx = x + move[direction][0]
    ny = y + move[direction][1]

    if arr[nx][ny] == 0 and my[nx][ny] == 0:
        my[nx][ny] = 1
        
        x = nx
        y = ny
        
        cnt += 1
        turn_time = 0
        
        continue
    
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - move[direction][0]
        ny = y - move[direction][1]

        if arr[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break

        turn_time = 0


print(cnt)

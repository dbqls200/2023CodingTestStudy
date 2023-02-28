# 120861 캐릭터의 좌표

def solution(keyinput, board):
    answer = [0, 0]
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    moves = {
        "up": [0, 1],
        "down": [0, -1],
        "left": [-1, 0],
        "right": [1, 0]
    }

    for key in keyinput:
        x, y = answer
        dx, dy = moves[key]
        x += dx
        y += dy
        if abs(x) > x_limit or abs(y) > y_limit:
            continue
        answer = x, y

    return answer

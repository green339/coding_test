# https://www.acmicpc.net/problem/20061

def down(idx, flag):  # 없어진 행
    if flag:
        board = green
    else:
        board = blue
    for r in range(idx, 0, -1):
        board[r] = board[r - 1]
    board[0] = [0, 0, 0, 0]


def locate(key, flag):
    global answer
    if flag:
        board = green
    else:
        board = blue
    if key == 1:
        for k in range(6):
            if board[k][y]:
                zero = k - 1
                break
        else:
            zero = 5
        board[zero][y] = 1
    elif key == 2:
        for k in range(6):
            if board[k][y] or board[k][y + 1]:
                zero = k - 1
                break
        else:
            zero = 5
        board[zero][y] = 1
        board[zero][y + 1] = 1
    elif key == 3:
        for k in range(6):
            if board[k][y]:
                zero = k - 1
                break
        else:
            zero = 5
        board[zero][y] = 1
        board[zero - 1][y] = 1
    i = 5
    while i > 0:
        if sum(board[i]) == 4:
            board[i] = [0, 0, 0, 0]
            answer += 1
            down(i, flag)
            continue
        i -= 1
        # 연한 부분에 있으면
        if i < 2:
            if sum(board[i]) > 0:
                board[5] = [0, 0, 0, 0]
                down(5, flag)
                i = 5


answer = 0
blue = [[0] * 4 for _ in range(6)]
green = [[0] * 4 for _ in range(6)]

N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
for t, x, y in blocks:
    locate(t, 1)
    y = abs(3 - x)
    if t == 2:
        t = 3
    elif t == 3:
        t = 2
        y -= 1
    locate(t, 0)
print(answer)
print(sum(map(sum, green)) + sum(map(sum, blue)))

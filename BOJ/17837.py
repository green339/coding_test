# https://www.acmicpc.net/problem/17837
from collections import deque


def white():
    move = deque()
    while arr[x][y][-1] != i:
        up_i = arr[x][y].pop()
        mal[up_i][0] = nx
        mal[up_i][1] = ny
        move.appendleft(up_i)
    move.appendleft(arr[x][y].pop())
    mal[i][0] = nx
    mal[i][1] = ny
    arr[nx][ny].extend(move)


def red():
    move = deque()
    while arr[x][y][-1] != i:
        up_i = arr[x][y].pop()
        mal[up_i][0] = nx
        mal[up_i][1] = ny
        move.append(up_i)
    move.append(arr[x][y].pop())
    mal[i][0] = nx
    mal[i][1] = ny
    arr[nx][ny].extend(move)


def blue():
    global d, nx, ny
    d = rev_dir[d]
    nx = x + direction[d][0]
    ny = y + direction[d][1]
    mal[i][2]=d
    if -1 < nx < N and -1 < ny < N:
        if board[nx][ny] == 0:
            white()
        elif board[nx][ny] == 1:
            red()
    else:
        blue()


mal = dict()
N, K = map(int, input().split())
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
rev_dir = {1: 2, 2: 1, 3: 4, 4: 3}
board = [list(map(int, input().split())) for _ in range(N)]
arr = [[deque() for _ in range(N)] for _ in range(N)]
for i in range(K):
    r, c, d = map(int, input().split())
    arr[r - 1][c - 1].append(i)
    mal[i] = [r-1, c-1, d]
turn = 1
for turn in range(1, 1002):
    for i in range(K):
        x, y, d = mal[i]
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if -1 < nx < N and -1 < ny < N:
            if board[nx][ny] == 0:
                white()
            elif board[nx][ny] == 1:
                red()
            elif board[nx][ny] == 2:
                blue()
        else:
            blue()
        if len(arr[nx][ny]) >= 4:
            break
    else:
        continue
    print(turn)
    break
else:
    print(-1)

# https://www.acmicpc.net/problem/15683

import sys

input = sys.stdin.readline


def up(sx, sy, flag):
    for nx in range(sx, -1, -1):
        if board[nx][sy] == 6:
            return
        if board[nx][sy] <= 0:
            board[nx][sy] += flag


def down(sx, sy, flag):
    for nx in range(sx, N):
        if board[nx][sy] == 6:
            return
        if board[nx][sy] <= 0:
            board[nx][sy] += flag


def right(sx, sy, flag):
    for ny in range(sy, M):
        if board[sx][ny] == 6:
            return
        if board[sx][ny] <= 0:
            board[sx][ny] += flag


def left(sx, sy, flag):
    for ny in range(sy, -1, -1):
        if board[sx][ny] == 6:
            return
        if board[sx][ny] <= 0:
            board[sx][ny] += flag


def dfs(idx):
    global answer
    if idx == len(cctv):
        tmp = 0
        for b in board:
            tmp += b.count(0)
        answer = min(answer, tmp)
        return
    x, y = cctv[idx]
    if board[x][y] == 1:
        left(x, y, -1)
        dfs(idx + 1)
        left(x, y, 1)

        right(x, y, -1)
        dfs(idx + 1)
        right(x, y, 1)

        up(x, y, -1)
        dfs(idx + 1)
        up(x, y, 1)

        down(x, y, -1)
        dfs(idx + 1)
        down(x, y, 1)

    elif board[x][y] == 2:
        left(x, y, -1)
        right(x, y, -1)
        dfs(idx + 1)
        left(x, y, 1)
        right(x, y, 1)

        up(x, y, -1)
        down(x, y, -1)
        dfs(idx + 1)
        up(x, y, 1)
        down(x, y, 1)

    elif board[x][y] == 3:
        up(x, y, -1)
        right(x, y, -1)
        dfs(idx + 1)
        up(x, y, 1)

        down(x, y, -1)
        dfs(idx + 1)
        right(x, y, 1)

        left(x, y, -1)
        dfs(idx + 1)
        down(x, y, 1)

        up(x, y, -1)
        dfs(idx + 1)
        left(x, y, 1)
        up(x, y, 1)

    elif board[x][y] == 4:
        left(x, y, -1)
        up(x, y, -1)
        right(x, y, -1)
        dfs(idx + 1)
        left(x, y, 1)

        down(x, y, -1)
        dfs(idx + 1)
        up(x, y, 1)

        left(x, y, -1)
        dfs(idx + 1)
        right(x, y, 1)

        up(x, y, -1)
        dfs(idx + 1)
        down(x, y, 1)
        left(x, y, 1)
        up(x, y, 1)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 5:
            cctv.append((i, j))
        elif board[i][j] == 5:
            left(i, j, -1)
            right(i, j, -1)
            up(i, j, -1)
            down(i, j, -1)
answer = N * M
dfs(0)
print(answer)

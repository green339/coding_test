# https://www.acmicpc.net/problem/15683
import sys
from copy import deepcopy

input = sys.stdin.readline


def up(x, y):
    for r in range(x, -1, -1):
        if graph[r][y] == 6:
            break
        elif graph[r][y] == 0:
            graph[r][y] = -1


def down(x, y):
    for r in range(x, N):
        if graph[r][y] == 6:
            break
        elif graph[r][y] == 0:
            graph[r][y] = -1


def left(x, y):
    for c in range(y, -1, -1):
        if graph[x][c] == 6:
            break
        elif graph[x][c] == 0:
            graph[x][c] = -1


def right(x, y):
    for c in range(y, M):
        if graph[x][c] == 6:
            break
        elif graph[x][c] == 0:
            graph[x][c] = -1


def watch(arr):
    if len(arr) == len(cctv):
        global graph
        graph = deepcopy(board)
        for k in range(len(arr)):
            d = arr[k]
            cx, cy = cctv[k]
            if d == 1:
                right(cx, cy)
            elif d == 2:
                left(cx, cy)
            elif d == 3:
                up(cx, cy)
            elif d == 4:
                down(cx, cy)
            elif d == 5:
                right(cx, cy)
                left(cx, cy)
            elif d == 6:
                up(cx, cy)
                down(cx, cy)
            elif d == 7:
                right(cx, cy)
                up(cx, cy)
            elif d == 8:
                right(cx, cy)
                down(cx, cy)
            elif d == 9:
                left(cx, cy)
                down(cx, cy)
            elif d == 10:
                left(cx, cy)
                up(cx, cy)
            elif d == 11:
                right(cx, cy)
                up(cx, cy)
                down(cx, cy)
            elif d == 12:
                right(cx, cy)
                left(cx, cy)
                down(cx, cy)
            elif d == 13:
                left(cx, cy)
                up(cx, cy)
                down(cx, cy)
            elif d == 14:
                right(cx, cy)
                left(cx, cy)
                up(cx, cy)
            elif d == 15:
                right(cx, cy)
                left(cx, cy)
                up(cx, cy)
                down(cx, cy)
        cnt = 0
        for g in graph:
            cnt += g.count(0)
        global ans
        ans = min(ans, cnt)
        return
    x, y = cctv[len(arr)]
    if board[x][y] == 1:
        for a in range(1, 5):
            watch(arr + [a])
    elif board[x][y] == 2:
        for b in range(5, 7):
            watch(arr + [b])
    elif board[x][y] == 3:
        for c in range(7, 11):
            watch(arr + [c])
    elif board[x][y] == 4:
        for d in range(11, 15):
            watch(arr + [d])
    elif board[x][y] == 5:
        watch(arr + [15])


if __name__ == "__main__":
    N, M = map(int, input().split())
    cctv = []
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(M):
            if 0 < board[i][j] < 6:
                cctv.append((i, j))
    ans = N * M
    watch([])
    print(ans)

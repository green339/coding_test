# https://www.acmicpc.net/problem/20057
import sys

input = sys.stdin.readline


def flow(d, x, y):
    global answer
    done = 0
    for k, v in d.items():
        if k == 0:
            continue
        cur = int(board[x][y] * k)
        for dx, dy in v:
            nx = x + dx
            ny = y + dy
            done += cur
            if -1 < nx < N and -1 < ny < N:
                board[nx][ny] += cur
            else:
                answer += cur
    nx = d[0][0][0] + x
    ny = d[0][0][1] + y
    if -1 < nx < N and -1 < ny < N:
        board[nx][ny] += (board[x][y] - done)
    else:
        answer += (board[x][y] - done)
    board[x][y] = 0


def left():
    d = {0.01: [(-1, 1), (1, 1)],
         0.02: [(-2, 0), (2, 0)],
         0.05: [(0, -2)],
         0.07: [(-1, 0), (1, 0)],
         0.1: [(-1, -1), (1, -1)],
         0: [(0, -1)]
         }

    for j in range(ty - 1, ty - 1 - t, -1):
        flow(d, tx, j)
    return j


def right():
    d = {0.01: [(-1, -1), (1, -1)],
         0.02: [(-2, 0), (2, 0)],
         0.05: [(0, 2)],
         0.07: [(-1, 0), (1, 0)],
         0.1: [(-1, 1), (1, 1)],
         0: [(0, 1)]
         }
    for j in range(ty + 1, ty + 1 + t):
        flow(d, tx, j)
    return j


def down():
    d = {0.01: [(-1, -1), (-1, 1)],
         0.02: [(0, -2), (0, 2)],
         0.05: [(2, 0)],
         0.07: [(0, -1), (0, 1)],
         0.1: [(1, -1), (1, 1)],
         0: [(1, 0)]
         }
    for i in range(tx + 1, tx + 1 + t):
        flow(d, i, ty)
    return i


def up():
    d = {0.01: [(1, -1), (1, 1)],
         0.02: [(0, -2), (0, 2)],
         0.05: [(-2, 0)],
         0.07: [(0, -1), (0, 1)],
         0.1: [(-1, -1), (-1, 1)],
         0: [(-1, 0)]
         }
    for i in range(tx - 1, tx - 1 - t, -1):
        flow(d, i, ty)
    return i


answer = 0
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

tx, ty = N // 2, N // 2
for t in range(1, N):
    if t % 2:
        ty = left()
        tx = down()
    else:
        ty = right()
        tx = up()
left()
print(answer)

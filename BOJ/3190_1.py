# https://www.acmicpc.net/problem/3190
import sys
from collections import deque


def move(dd):
    nh = [snake[0][0] + d[dd][0], snake[0][1] + d[dd][1]]
    if -1 < nh[0] < N and -1 < nh[1] < N:
        if board[nh[0]][nh[1]] == 1:
            board[nh[0]][nh[1]] = 2
            snake.appendleft(nh)
        elif board[nh[0]][nh[1]] == 0:
            board[nh[0]][nh[1]] = 2
            snake.appendleft(nh)
            tx, ty = snake.pop()
            board[tx][ty] = 0
        else:  # 자신이랑 만남
            return False
    else:  # 벽이랑 만남
        return False
    return True


input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
board[0][0] = 2
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
snake = deque()
snake.append([0, 0])
direction = 0
L = int(input())
t = 0
for _ in range(L):
    x, c = input().strip().split()
    x = int(x)
    while t < x:
        t += 1
        if not move(direction):
            break
    else:
        t += 1
        # 회전
        if c == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        # 이동
        if not move(direction):
            break
        continue
    break
else:
    while True:
        t += 1
        if not move(direction):
            break
print(t)

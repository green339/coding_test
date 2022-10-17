# https://www.acmicpc.net/problem/14499
import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
down = 1
front = 5
right = 3
for c in cmd:
    nx = direction[c][0] + x
    ny = direction[c][1] + y
    # print(c,down,front,right)
    if -1 < nx < N and -1 < ny < M:
        x = nx
        y = ny
        tmp = down
        if c == 1: # 동
            down = right
            right = 7 - tmp
        elif c == 2: # 서
            down = 7 - right
            right = tmp
        elif c == 3: # 북
            down = 7 - front
            front = tmp
        elif c == 4: # 남
            down = front
            front = 7 - tmp
        if board[x][y]:
            dice[down] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[down]
        print(dice[7 - down])

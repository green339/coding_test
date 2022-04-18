# https://www.acmicpc.net/problem/15685
import sys
input = sys.stdin.readline

N = int(input())
dragon = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 101 for _ in range(101)]
direction = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
for x, y, d, g in dragon:
    board[x][y] = 1
    # 0 세대
    x += direction[d][0]
    y += direction[d][1]
    board[x][y] = 1
    move = [d]
    # 1~N 세대
    for gen in range(g):
        for i in range(2 ** gen - 1, -1, -1):
            d = (move[i] + 1) % 4
            x += direction[d][0]
            y += direction[d][1]
            board[x][y] = 1
            move.append(d)
answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            if board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
                answer += 1
print(answer)

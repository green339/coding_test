# https://www.acmicpc.net/problem/15684
import sys

input = sys.stdin.readline


def move():
    for i in range(N):
        ci = i
        for cj in range(H):
            if ci > 0 and board[ci - 1][cj]:  # 왼쪽에 가로선 있는 경우
                ci -= 1
                continue
            if board[ci][cj]:  # 자기 자신에서 가로선 있는 경우
                ci += 1
        if ci != i:
            return False
    return True


def dfs(depth, r, c):
    global answer
    if answer <= depth:
        return
    if move():
        answer = min(depth, answer)
        return
    if depth == 3:
        return
    for x in range(r, N - 1):
        if x > r:
            c = 0
        for y in range(c, H):
            if not board[x][y] and not board[x + 1][y]:
                if x > 0 and board[x - 1][y]:
                    continue
                board[x][y] = 1
                dfs(depth + 1, x, y)
                board[x][y] = 0


answer = 4
N, M, H = map(int, input().split())
board = [[0] * H for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    board[b - 1][a - 1] = 1
dfs(0, 0, 0)
print(answer if answer < 4 else -1)

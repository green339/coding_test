# https://www.acmicpc.net/problem/17142
import sys
from collections import deque

input = sys.stdin.readline
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    visited = [[0] * N for _ in range(N)]
    q = deque()
    for sx, sy in select:
        q.append((0, sx, sy))
        visited[sx][sy] = 1
    res = 0
    while q:
        t, x, y = q.popleft()
        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if -1 < nx < N and -1 < ny < N:
                if not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        continue
                    visited[nx][ny] = 1
                    if board[nx][ny] == 0:
                        res += 1
                    elif board[nx][ny] == 2 and res == zeros: # 모든 칸이 바이러스 있으면 지나갈 필요가 없음
                        continue
                    q.append((t + 1, nx, ny))
    if res == zeros:
        return t
    else:
        return 10e9


def dfs(depth, idx):
    global answer
    if depth == M:
        answer = min(answer, bfs())
    for i in range(idx, len(cand)):
        if cand[i] not in select:
            select.add(cand[i])
            dfs(depth + 1, i + 1)
            select.remove(cand[i])


answer = 10e9
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cand = []
select = set()
zeros = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            cand.append((i, j))
        elif board[i][j] == 0:
            zeros += 1
dfs(0, 0)
print(answer if answer != 10e9 else -1)

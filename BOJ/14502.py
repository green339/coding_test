# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
import copy

input = sys.stdin.readline


def dfs(depth, si, sj):
    global answer
    if depth == 3:
        arr = copy.deepcopy(board)
        q = copy.deepcopy(dq)
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < N and -1 < ny < M:
                    if arr[nx][ny] == 0:
                        q.append((nx, ny))
                        arr[nx][ny] = 2
        tmp = 0
        for a in arr:
            tmp += a.count(0)
        answer = max(answer, tmp)
        return
    for i in range(si, N):
        if i > si:
            sj = 0
        for j in range(sj, M):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(depth + 1, i, j)
                board[i][j] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dq = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            dq.append((i, j))
answer = 0
dfs(0, 0, 0)
print(answer)

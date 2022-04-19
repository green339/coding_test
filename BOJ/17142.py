# https://www.acmicpc.net/problem/17142
import sys
from collections import deque

input = sys.stdin.readline
direction = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs():
    global answer
    cnt = zeros
    arr = [[0] * N for _ in range(N)]
    q = deque()
    for v in range(virus_cnt):
        if visited[v]:
            q.append((virus[v][0], virus[v][1]))
            arr[virus[v][0]][virus[v][1]] = 1
    while q:
        vx, vy = q.popleft()
        last = arr[vx][vy]
        for dx, dy in direction:
            nx = dx + vx
            ny = dy + vy
            if -1 < nx < N and -1 < ny < N and not arr[nx][ny]:
                if not board[nx][ny]:
                    q.append((nx, ny))
                    arr[nx][ny] = arr[vx][vy] + 1
                    cnt -= 1
                elif board[nx][ny] == 2 and cnt:  # 비활성->활성 (이미 바이러스가 있으니까 지나가야 하는 경우에 대해서만 count)
                    q.append((nx, ny))
                    arr[nx][ny] = arr[vx][vy]+1

    if not cnt:
        answer = min(answer, last - 1)


def dfs(depth, idx):
    if depth == M:
        bfs()
        return
    for x in range(idx, virus_cnt):
        if not visited[x]:
            visited[x] = 1
            dfs(depth + 1, x + 1)
            visited[x] = 0


N, M = map(int, input().split())
board = []
virus = []
virus_cnt = 0
zeros = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[-1][j] == 2:
            virus.append((i, j))
            virus_cnt += 1
        elif board[-1][j] == 0:
            zeros += 1
visited = [0] * virus_cnt
answer = 1e9
dfs(0, 0)
print(-1 if answer == 1e9 else answer)

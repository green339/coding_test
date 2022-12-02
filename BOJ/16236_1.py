# https://www.acmicpc.net/problem/16236
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs(sx, sy, size):
    q = deque()
    q.append((sx, sy))
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    cand=[]
    while q:
        x, y = q.popleft()
        if cand and visited[x][y]-1>cand[0][0]:
            continue
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < N:
                if visited[nx][ny]:
                    continue
                visited[nx][ny] += (visited[x][y] + 1)
                if board[nx][ny] == 0 or board[nx][ny] == size:  # 지나간다
                    q.append((nx, ny))
                elif board[nx][ny] < size:  # 먹을 수 있다.
                    cand.append((visited[nx][ny]-1,nx,ny))
    if cand:
        return sorted(cand)[0]
    return -1, N, N


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            si = i
            sj = j
            board[i][j] = 0
            break
    else:
        continue
    break
t = 0
cur = 2
eat = 0
while True:
    cost,si, sj= bfs(si, sj, cur)
    if si == N:
        print(t)
        break
    # 물고기를 먹는다.
    board[si][sj] = 0
    eat += 1
    if eat == cur:
        cur += 1
        eat = 0
    t += cost

# https://www.acmicpc.net/problem/17142
from collections import deque

d = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def spread():
    global ans
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.extend(visited_virus)
    for qx, qy in q:
        visited[qx][qy] = 1
    t = 0
    while q:
        x, y = q.popleft()
        if not board[x][y]:
            t = visited[x][y] - 1
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < N and not visited[nx][ny]:
                if not board[nx][ny] or board[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    for a in range(N):
        for b in range(N):
            if not (board[a][b] | visited[a][b]):
                return
    ans = min(ans, t)


def comb(depth, idx):
    if depth == M:
        spread()
        return
    for x in range(idx, virus_cnt):
        visited_virus.add((virus[x]))
        comb(depth + 1, x + 1)
        visited_virus.remove((virus[x]))


ans = 1e9
N, M = map(int, input().split())
virus = dict()
visited_virus = set()
virus_cnt = 0
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[-1][j] == 2:
            virus[virus_cnt] = (i, j)
            virus_cnt += 1
comb(0, 0)
print(ans if ans < 1e9 else -1)

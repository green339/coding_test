# https://www.acmicpc.net/problem/1261
import sys
import heapq

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
q = []
heapq.heappush(q, (0, 0, 0))
dist = [[1e9] * M for _ in range(N)]
dist[0][0] = 0
while q:
    wall, cx, cy = heapq.heappop(q)
    if dist[cx][cy] < wall:
        continue
    if cx == N - 1 and cy == M - 1:
        break
    for d in range(4):
        nx = cx + dx[d]
        ny = cy + dy[d]
        if -1 < nx < N and -1 < ny < M:
            tmp = board[nx][ny] + wall
            if tmp < dist[nx][ny]:
                dist[nx][ny] = tmp
                heapq.heappush(q, (tmp, nx, ny))
print(dist[-1][-1])

# https://www.acmicpc.net/problem/1926
import sys
from collections import deque
input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0
area = 0
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            cnt += 1
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            tmp = 0
            while q:
                x, y = q.popleft()
                tmp += 1
                for dx, dy in d:
                    nx = dx + x
                    ny = dy + y
                    if -1 < nx < n and -1 < ny < m:
                        if board[nx][ny] and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = 1
            area = max(tmp, area)
print(cnt)
print(area)

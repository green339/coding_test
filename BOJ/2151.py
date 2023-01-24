# https://www.acmicpc.net/problem/2151
import sys
import heapq

input = sys.stdin.readline
d = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}


def bfs():
    visited = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
    q = []
    for dd in range(4):
        q.append((0, m[0][0], m[0][1], dd))
        visited[m[0][0]][m[0][1]][dd] = 1
    while q:
        cnt, x, y, cur = heapq.heappop(q)
        if x == m[1][0] and y == m[1][1]:
            return cnt
        nx = d[cur][0] + x
        ny = d[cur][1] + y
        if -1 < nx < n and -1 < ny < n:
            if not visited[nx][ny][cur]:
                visited[nx][ny][cur] = 1
                if board[nx][ny] != "*":
                    if board[nx][ny] == "!":
                        # 거울 설치
                        q.append((cnt + 1, nx, ny, (cur + 1) % 4))
                        q.append((cnt + 1, nx, ny, (cur - 1) % 4))
                    # 거울 설치X 거나 . or #
                    q.append((cnt, nx, ny, cur))


n = int(input())
m = []
board = []
for i in range(n):
    tmp = list(input().strip())
    for j in range(n):
        if tmp[j] == "#":
            m.append((i, j))
    board.append(tmp)
print(bfs())

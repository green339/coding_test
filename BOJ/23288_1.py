# https://www.acmicpc.net/problem/23288
from collections import deque

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def score(sx, sy):
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1
    q = deque()
    q.append((sx, sy))
    res=1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] == board[sx][sy] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    res+=1
                    q.append((nx, ny))
    return res * board[sx][sy]


answer = 0
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
i = 0
j = 0
dd = 0
up = 1
right = 3
front = 5
for _ in range(K):
    i += d[dd][0]
    j += d[dd][1]
    if i < 0 or i >= N or j < 0 or j >= M:
        i -= d[dd][0] * 2
        j -= d[dd][1] * 2
        dd = (dd + 2) % 4
    if dd == 0:
        tmp = up
        up = 7 - right
        right = tmp
    elif dd == 1:
        tmp = up
        up = 7 - front
        front = tmp
    elif dd == 2:
        tmp = up
        up = right
        right = 7 - tmp
    elif dd == 3:
        tmp = up
        up = front
        front = 7 - tmp
    answer += score(i, j)
    if board[i][j] > 7 - up:
        dd = (dd - 1) % 4
    elif board[i][j] < 7 - up:
        dd = (dd + 1) % 4

print(answer)

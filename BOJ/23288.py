# # https://www.acmicpc.net/problem/23288
# 1:34
from collections import deque


def move(dd):
    global bottom, right, front
    if dd == 0:
        tmp = bottom
        bottom = right
        right = 7 - tmp
    elif dd == 1:
        tmp = bottom
        bottom = front
        front = 7 - tmp
    elif dd == 2:
        tmp = bottom
        bottom = 7 - right
        right = tmp
    elif dd == 3:
        tmp = bottom
        bottom = 7 - front
        front = tmp


direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

answer = 0
sx = 0
sy = 0
bottom = 6
right = 3
front = 5
sd = 0
for _ in range(K):
    # 일단 이동을 하고
    sx += direction[sd][0]
    sy += direction[sd][1]
    if not (-1 < sx < N and -1 < sy < M):
        sd = (sd + 2) % 4
        sx += direction[sd][0] * 2
        sy += direction[sd][1] * 2
    move(sd)
    answer += board[sx][sy]
    q = deque()
    q.append((sx, sy))
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1
    while q:
        vx, vy = q.popleft()
        for dx, dy in direction.values():
            nx = vx + dx
            ny = vy + dy
            if -1 < nx < N and -1 < ny < M and not visited[nx][ny]:
                if board[nx][ny] == board[vx][vy]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    answer += board[vx][vy]
    # 다음 방향
    if board[sx][sy] < bottom:
        sd = (sd + 1) % 4
    elif board[sx][sy] > bottom:
        sd = (sd - 1) % 4
print(answer)

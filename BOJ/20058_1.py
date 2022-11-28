# https://www.acmicpc.net/problem/20058
import sys
from collections import deque

input = sys.stdin.readline


def rotate_90(p):
    plen = 2 ** p
    for i in range(0, rc, plen):
        for j in range(0, rc, plen):
            tmp = board[i:i + plen]
            for k in range(plen):
                tmp[k] = tmp[k][j:j + plen]
            tmp = list(zip(*tmp))
            for k in range(2 ** p):
                board[i + k][j:j + 2 ** p] = tmp[k][::-1]


N, Q = map(int, input().split())
rc = 2 ** N
board = [list(map(int, input().split())) for _ in range(rc)]
L = list(map(int, input().split()))

for stage in L:
    rotate_90(stage)
    melt = [b[:] for b in board]
    for r in range(rc):
        for c in range(rc):
            if not board[r][c]:
                continue
            cnt = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if -1 < nr < rc and -1 < nc < rc:
                    if board[nr][nc]:
                        cnt += 1
            if cnt < 3:
                melt[r][c] -= 1
    board = melt

ices = 0
group = 0
visited = [[0] * rc for _ in range(rc)]
for r in range(rc):
    for c in range(rc):
        if not visited[r][c] and board[r][c]:
            ices += board[r][c]
            q = deque()
            q.append((r, c))
            visited[r][c] = 1
            cnt = 1
            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if -1 < nx < rc and -1 < ny < rc:
                        if not visited[nx][ny] and board[nx][ny]:
                            visited[nx][ny] = 1
                            visited[nx][ny] = 1
                            cnt += 1
                            ices += board[nx][ny]
                            q.append((nx, ny))
            group = max(group, cnt)
print(ices)
print(group)

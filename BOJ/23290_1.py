# https://www.acmicpc.net/problem/23290
import sys
from copy import deepcopy
from collections import deque


def fish_move():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            while board[r][c]:
                dd = board[r][c].pop()
                for idx in range(8):
                    nd = (dd - idx) % 8
                    nr = r + d[nd][0]
                    nc = c + d[nd][1]
                    if nr == sx and nc == sy:
                        continue
                    if -1 < nr < 4 and -1 < nc < 4:
                        if smell[nr][nc] < t:
                            res[nr][nc].append(nd)
                            break
                else:
                    res[r][c].append(dd)
    return res


def shark_move(cur):
    global sx, sy
    q = deque()
    q.append((sx, sy, [],0))
    res = -1
    while q:
        x, y, route, cnt = q.popleft()
        if len(route) == 3:
            if res < cnt:
                res = cnt
                fish_route = route
            continue
        for idx in [2, 0, 6, 4]:
            nx = x + d[idx][0]
            ny = y + d[idx][1]
            if -1 < nx < 4 and -1 < ny < 4:
                if (nx, ny) in route:
                    ate = 0
                else:
                    ate = len(board[nx][ny])
                q.append((nx, ny, route + [(nx, ny)], cnt + ate))
    for frx, fry in set(fish_route):
        if board[frx][fry]:
            smell[frx][fry] = cur + 2
            board[frx][fry] = []
    sx = fish_route[-1][0]
    sy = fish_route[-1][1]


input = sys.stdin.readline
d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

board = [[[] for _ in range(4)] for _ in range(4)]
smell = [[-1] * 4 for _ in range(4)]  # 물고기 냄새
M, S = map(int, input().split())
for _ in range(M):
    fx, fy, fd = map(int, input().split())
    board[fx - 1][fy - 1].append(fd - 1)
sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for t in range(S):
    #  복제 마법
    arr = deepcopy(board)
    #   물고기 이동
    board = deepcopy(fish_move())
    # 상어 이동
    shark_move(t)
    # 물고기 복제
    for i in range(4):
        for j in range(4):
            if arr[i][j]:
                for a in arr[i][j]:
                    board[i][j].append(a)


answer = 0
for i in range(4):
    for j in range(4):
        answer += len(board[i][j])
print(answer)

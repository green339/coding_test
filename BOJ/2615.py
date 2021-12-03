# https://www.acmicpc.net/problem/2615
import sys
from collections import deque

d = {1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0)}


def omok(sx, sy):
    color = arr[sx][sy]
    q = deque()
    for i in range(1, 5):
        q.append((1, sx, sy, i))
    while q:
        cnt, nx, ny, dd = q.popleft()
        vx = d[dd][0] + nx
        vy = d[dd][1] + ny
        if -1 < vx < 19 and -1 < vy < 19:
            if arr[vx][vy] == color:
                q.append((cnt + 1, vx, vy, dd))
                continue
        if cnt == 5 and arr[sx - d[dd][0]][sy - d[dd][1]] != color:  # 육목인지 체크
            return color
    return 0


arr = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
flag=0
for x in range(19):
    if flag:
        break
    for y in range(19):
        if arr[x][y]:
            flag = omok(x, y)
            if flag:
                print(flag)
                print(x + 1, y + 1)
                break
if not flag:
    print(0)

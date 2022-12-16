# https://www.acmicpc.net/problem/20061
from collections import deque
import sys

input = sys.stdin.readline
blue = [deque([0, 0, 0, 0, 0, 0]) for _ in range(4)]
green = deque([[0, 0, 0, 0] for _ in range(6)])
N = int(input())
tt = {1: (0, 0), 2: (0, 1), 3: (1, 0)}
answer = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    # 파랑에 넣기
    x1 = x
    x2 = x + tt[t][0]
    sy = 5
    for j in range(5, -1, -1):
        if not blue[x1][j] and not blue[x2][j]:
            sy = j
        else:
            break
    y1 = sy
    y2 = sy + tt[t][1]
    blue[x1][y1] = 1
    blue[x2][y2] = 1
    #  y1,y2에 들어왓으니까 이걸 조사
    delete = set()
    for j in [y1, y2]:
        for i in range(4):
            if blue[i][j] != 1:
                break
        else:
            delete.add(j)
    answer += len(delete)
    for d in sorted(delete, reverse=True):
        for j in range(d, 5):
            for i in range(4):
                blue[i][j] = blue[i][j + 1]
        for i in range(4):
            blue[i][-1] = 0
    cnt = 0
    for j in [4, 5]:
        for i in range(4):
            if blue[i][j] == 1:
                cnt += 1
                break
        else:
            break
    for i in range(4):
        blue[i].rotate(-cnt)
    for j in [4, 5]:
        for i in range(4):
            blue[i][j] = 0
    # 초록에 넣기
    y1 = y
    y2 = y + tt[t][1]
    sx = 5
    for i in range(5, -1, -1):
        if not green[i][y1] and not green[i][y2]:
            sx = i
        else:
            break
    x1 = sx
    x2 = sx + tt[t][0]
    green[x1][y1] = 1
    green[x2][y2] = 1
    delete = set()
    for i in [x1, x2]:
        for j in range(4):
            if green[i][j] != 1:
                break
        else:
            delete.add(i)
    answer += len(delete)
    for d in sorted(delete, reverse=True):
        for i in range(d, 5):
            for j in range(4):
                green[i][j] = green[i + 1][j]
        for j in range(4):
            green[-1][j] = 0
    cnt = 0
    for i in [4, 5]:
        for j in range(4):
            if green[i][j] == 1:
                cnt += 1
                break
        else:
            break
    green.rotate(-cnt)
    for i in [4, 5]:
        for j in range(4):
            green[i][j] = 0

print(answer)
c = 0
for g in green:
    c += g.count(1)
for b in blue:
    c += b.count(1)
print(c)
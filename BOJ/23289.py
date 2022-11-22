# https://www.acmicpc.net/problem/23289
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dd = {1: [(-1, 1), (0, 1), (1, 1)],
      2: [(-1, -1), (0, -1), (1, -1)],
      3: [(-1, -1), (-1, 0), (-1, 1)],
      4: [(1, -1), (1, 0), (1, 1)]}


def wind():
    for hx, hy, hd in heat:
        res = [[0] * C for _ in range(R)]
        res[hx][hy] = 5
        q = deque()
        q.append((hx, hy))
        while q:
            x, y = q.popleft()
            if not res[x][y]:
                continue
            for dx, dy in dd[hd]:
                # 방향이 오른쪽 왼쪽인 경우
                if hd < 3:
                    if dx == -1:
                        if walls[x][y][0]:
                            continue
                    elif dx == 1:
                        if walls[x][y][2]:
                            continue
                # 방향이 위 아래 인 경우
                else:
                    if dy == -1:
                        if walls[x][y][3]:
                            continue
                    elif dy == 1:
                        if walls[x][y][1]:
                            continue
                nx = x + dx
                ny = y + dy
                if -1 < nx < R and -1 < ny < C:
                    if res[nx][ny]:
                        continue
                    # 방향이 오른쪽 왼쪽인 경우
                    if hd < 3:
                        if dy == -1:
                            if walls[nx][ny][1]:
                                continue
                        elif dy == 1:
                            if walls[nx][ny][3]:
                                continue
                    # 방향이 위 아래 인 경우
                    else:
                        if dx == -1:
                            if walls[nx][ny][2]:
                                continue
                        elif dx == 1:
                            if walls[nx][ny][0]:
                                continue
                    res[nx][ny] = res[x][y] - 1
                    q.append((nx, ny))
        for i in range(R):
            for j in range(C):
                temperature[i][j] += res[i][j]


def control():
    res = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for idx in range(1, 3):
                if walls[i][j][idx]:
                    continue
                ni = i + d[idx][0]
                nj = j + d[idx][1]
                if -1 < ni < R and -1 < nj < C:
                    a = abs(temperature[i][j] - temperature[ni][nj]) // 4
                    if temperature[i][j] > temperature[ni][nj]:
                        res[i][j] -= a
                        res[ni][nj] += a
                    else:
                        res[i][j] += a
                        res[ni][nj] -= a
    for i in range(R):
        for j in range(C):
            temperature[i][j] += res[i][j]


def check():
    for cx, cy in test:
        if temperature[cx][cy] < K:
            return False
    return True


R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = [[[0, 0, 0, 0] for _ in range(C)] for _ in range(R)]

for _ in range(W):
    x, y, t = map(int, input().split())
    walls[x - 1][y - 1][t] = 1
    if t == 0:
        walls[x - 2][y - 1][2] = 1
    else:
        walls[x - 1][y][3] = 1

heat = []
test = []
for x in range(R):
    for y in range(C):
        if board[x][y] == 1:
            if y < C - 1:
                heat.append((x, y + 1, board[x][y]))
        elif board[x][y] == 2:
            if y > 0:
                heat.append((x, y - 1, board[x][y]))
        elif board[x][y] == 3:
            if x > 0:
                heat.append((x - 1, y, board[x][y]))
        elif board[x][y] == 4:
            if x < R - 1:
                heat.append((x + 1, y, board[x][y]))
        elif board[x][y] == 5:
            test.append((x, y))
answer = 0
temperature = [[0] * C for _ in range(R)]
while answer <= 101:
    # 온풍기 바람
    wind()
    # 온도 조절
    control()
    # 바깥쪽 같의 온도가 1씩 감소
    for y in range(C):
        if temperature[0][y]:
            temperature[0][y] -= 1
        if temperature[-1][y]:
            temperature[-1][y] -= 1
    for x in range(1, R - 1):
        if temperature[x][0]:
            temperature[x][0] -= 1
        if temperature[x][-1]:
            temperature[x][-1] -= 1
    # 초콜릿 먹는다
    answer += 1
    # 조사하는 칸의 온도 k이상
    if check():
        break
print(min(answer, 101))
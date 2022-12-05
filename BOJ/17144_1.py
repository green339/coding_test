# https://www.acmicpc.net/problem/17144
import sys

input = sys.stdin.readline
d = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def spread():
    dust = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] < 1:
                continue
            dd = []
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < R and -1 < ny < C:
                    if A[nx][ny] == -1:
                        continue
                    dd.append((nx, ny))
            for ddx, ddy in dd:
                dust[ddx][ddy] += A[x][y] // 5
            A[x][y] -= (A[x][y] // 5) * len(dd)
    for x in range(R):
        for y in range(C):
            A[x][y] += dust[x][y]


def operate(flag, x, y):
    idx = 0
    prior = 0
    while y < C - 1:
        y += d[idx][1]
        tmp = A[x][y]
        A[x][y] = prior
        prior = tmp
    idx = (idx + flag) % 4
    while 0 < x < R - 1:
        x += d[idx][0]
        tmp = A[x][y]
        A[x][y] = prior
        prior = tmp
    idx = (idx + flag) % 4
    while 0 < y:
        y += d[idx][1]
        tmp = A[x][y]
        A[x][y] = prior
        prior = tmp
    idx = (idx + flag) % 4
    while True:
        x += d[idx][0]
        tmp = A[x][y]
        if tmp==-1:
            break
        A[x][y] = prior
        prior = tmp

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
air = []
for i in range(R):
    if A[i][0] == -1:
        air.append((i, 0))

for _ in range(T):
    spread()
    operate(1, air[0][0], air[0][1])
    operate(-1, air[1][0], air[1][1])

print(2 + sum(list(map(sum, A))))

# https://www.acmicpc.net/problem/17822
# 11:26
from collections import deque

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    global cnt
    dq = deque([(p, q) for p in range(1, N + 1) for q in range(M)])
    zero = set()
    while dq:
        i, j = dq.popleft()
        if circle[i][j] == 0:
            continue
        for di, dj in direction:
            ni = i + di
            nj = (j + dj) % M
            if 0 < ni <= N and (ni, nj) not in zero:
                if circle[ni][nj] == circle[i][j]:
                    dq.append((ni, nj))
                    zero.add((ni, nj))
                    zero.add((i, j))
    for zi, zj in zero:
        cnt -= 1
        circle[zi][zj] = 0

    if not zero and cnt:
        avg = sum(map(sum, circle.values())) / cnt
        for i in range(1, N + 1):
            for j in range(M):
                if circle[i][j]:
                    if circle[i][j] > avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < avg:
                        circle[i][j] += 1


N, M, T = map(int, input().split())
circle = dict()
for a in range(1, N + 1):
    circle[a] = deque(map(int, input().split()))

cnt = N * M
for _ in range(T):
    x, d, k = map(int, input().split())
    for a in range(x, N + 1, x):
        if d:
            circle[a].rotate(-k)
        else:
            circle[a].rotate(k)
    bfs()

print(sum(map(sum, circle.values())))

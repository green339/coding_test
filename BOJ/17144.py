# https://www.acmicpc.net/problem/17144
# 2:55
d = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def spread():
    arr = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] > 0:
                cnt = 0
                dust = A[x][y] // 5
                for dx, dy in d:
                    nx = dx + x
                    ny = dy + y
                    if -1 < nx < R and -1 < ny < C:
                        if not (ny == 0 and nx in air):
                            cnt += 1
                            arr[nx][ny] += dust
                arr[x][y] += A[x][y] - dust * cnt
    for x in range(R):
        for y in range(C):
            A[x][y] = arr[x][y]


def clean():
    prior = 0
    for idx in range(1, len(up)):
        temp = A[up[idx][0]][up[idx][1]]
        A[up[idx][0]][up[idx][1]] = prior
        prior = temp
    prior = 0
    for idx in range(1, len(down)):
        temp = A[down[idx][0]][down[idx][1]]
        A[down[idx][0]][down[idx][1]] = prior
        prior = temp


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
up = []
down = []
air = set()
for k in range(R):
    if A[k][0] == -1 and up:
        air.add(k)
        for j in range(C):
            down.append((k, j))
        for i in range(k + 1, R):
            down.append((i, -1))
        for j in range(C - 2, 0, -1):
            down.append((-1, j))
        for i in range(R - 1, k, -1):
            down.append((i, 0))
    elif A[k][0] == -1 and not up:
        air.add(k)
        for j in range(C):
            up.append((k, j))
        for i in range(k - 1, -1, -1):
            up.append((i, -1))
        for j in range(C - 2, 0, -1):
            up.append((0, j))
        for i in range(k):
            up.append((i, 0))
for _ in range(T):
    spread()
    clean()

answer = sum(map(sum, A))
print(answer)

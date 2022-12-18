# https://www.acmicpc.net/problem/21610
import sys

input = sys.stdin.readline

d = {1: (0, - 1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cloud = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}

for _ in range(M):
    dd, ss = map(int, input().split())
    move_cloud = set()
    for cx, cy in cloud:
        nx = (cx + d[dd][0] * ss) % N
        ny = (cy + d[dd][1] * ss) % N
        move_cloud.add((nx, ny))
        A[nx][ny] += 1
    cloud = set()
    for mcx, mcy in move_cloud:
        cnt = 0
        for di in [2, 4, 6, 8]:
            nx = mcx + d[di][0]
            ny = mcy + d[di][1]
            if -1 < nx < N and -1 < ny < N:
                if A[nx][ny]:
                    cnt += 1
        A[mcx][mcy] += cnt
    for i in range(N):
        for j in range(N):
            if (i, j) in move_cloud:
                continue
            if A[i][j] > 1:
                A[i][j] -= 2
                cloud.add((i, j))
print(sum(map(sum, A)))

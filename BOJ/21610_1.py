# https://www.acmicpc.net/problem/21610
# 8:10

direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(M)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for d, s in command:
    q = set()
    while cloud:
        x, y = cloud.pop()
        mx = (x + direction[d][0] * s) % N
        my = (y + direction[d][1] * s) % N
        A[mx][my] += 1
        q.add((mx, my))
    for x, y in q:
        cnt = 0
        for i in [2, 4, 6, 8]:
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if -1 < nx < N and -1 < ny < N and A[nx][ny]:
                cnt += 1
        A[x][y] += cnt
    for r in range(N):
        for c in range(N):
            if (r, c) in q:
                continue
            if A[r][c] > 1:
                cloud.append((r, c))
                A[r][c] -= 2
print(sum(map(sum, A)))

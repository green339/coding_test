# https://www.acmicpc.net/problem/11724
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

d = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

if __name__ == "__main__":
    M, N, H = map(int, input().split())
    box = defaultdict(list)
    q = deque()
    todo = 0
    cur = 1
    for k in range(H):
        for i in range(N):
            box[k].append(list(map(int, input().split())))
            for j, b in enumerate(box[k][i]):
                if b == 1:
                    q.append((i, j, k))
                elif b == 0:
                    todo += 1
    while q and todo > 0:
        vx, vy, vz = q.popleft()
        for dx, dy, dz in d:
            nx = dx + vx
            ny = dy + vy
            nz = dz + vz
            if -1 < nx < N and -1 < ny < M and -1 < nz < H:
                if not box[nz][nx][ny]:
                    q.append((nx, ny, nz))
                    box[nz][nx][ny] = box[vz][vx][vy] + 1
                    todo -= 1
                    cur = box[nz][nx][ny]
    print(cur - 1 if not todo else -1)

# https://www.acmicpc.net/problem/14891
from collections import deque

wheel = [deque(map(int, list(input().strip()))) for _ in range(4)]
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    q = deque()
    q.append((a - 1, b))
    visited = [0] * 4
    visited[a - 1] = 1
    todo = [(a - 1, b)]
    while q:
        x, r = q.popleft()
        for dx in [1, -1]:
            nx = x + dx
            if -1 < nx < 4 and visited[nx] == 0:
                visited[nx] = 1
                if dx == 1:
                    if wheel[x][2] != wheel[nx][6]:  # 회전
                        todo.append((nx, -r))
                        q.append((nx, -r))

                elif dx == -1:
                    if wheel[nx][2] != wheel[x][6]:  # 회전
                        todo.append((nx, -r))
                        q.append((nx, -r))
    for tdx,tdr in todo:
        wheel[tdx].rotate(tdr)
print(sum([2 ** i for i in range(4) if wheel[i][0]]))

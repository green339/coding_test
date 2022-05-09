# https://www.acmicpc.net/problem/13913
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([(0, N)])
visited = [-1] * 100001
visited[N] = N
while q:
    t, x = q.popleft()
    if x == K:
        break
    for dx in [-1, 1, x]:
        nx = dx + x
        if 0 <= nx <= 100000 and visited[nx] == -1:
            visited[nx] = x
            q.append((t + 1, nx))
print(t)
idx = K
path = [idx]
while idx != N:
    path.append(visited[idx])
    idx = visited[idx]
print(*path[::-1])

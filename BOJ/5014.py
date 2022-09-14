# https://www.acmicpc.net/problem/5014
import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [-1] * (f + 1)
q = deque()
q.append(s)
visited[s] = 0
while q:
    x = q.popleft()
    for dx in [u, -d]:
        nx = dx + x
        if 0 < nx <= f:
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)
print(visited[g] if visited[g] != -1 else "use the stairs")

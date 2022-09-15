# https://www.acmicpc.net/problem/9019
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    start, dest = map(int, input().split())
    q = deque()
    q.append(start)
    visited = ['' for _ in range(10000)]
    visited[start]=' '
    while q:
        x = q.popleft()
        if x == dest:
            break
        nx = (2 * x) % 10000
        if not visited[nx]:
            visited[nx] = visited[x] + 'D'
            q.append(nx)
        nx = (x - 1) % 10000
        if not visited[nx]:
            visited[nx] = visited[x] + 'S'
            q.append(nx)
        nx = x // 1000 + (x % 1000) * 10
        if not visited[nx]:
            visited[nx] = visited[x] + 'L'
            q.append(nx)
        nx = x // 10 + (x % 10) * 1000
        if not visited[nx]:
            visited[nx] = visited[x] + 'R'
            q.append(nx)
    print(visited[dest].lstrip())

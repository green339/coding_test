# https://www.acmicpc.net/problem/9205
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((hx, hy))
    visited = set()
    visited.add((hx, hy))
    while q:
        x, y = q.popleft()
        if abs(fx - x) + abs(fy - y) <= 1000:
            return "happy"
        for nx, ny in store:
            if (nx, ny) not in visited:
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx, ny))
                    visited.add((nx, ny))
    return "sad"


t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    store = set()
    for _ in range(n):
        store.add(tuple(map(int, input().split())))
    fx, fy = map(int, input().split())
    print(bfs())

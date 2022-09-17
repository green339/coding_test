# https://www.acmicpc.net/problem/1707
import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        x = q.popleft()
        for nx in board[x]:
            if visited[nx] == visited[x]:
                return False
            if not visited[nx]:
                visited[nx] = -visited[x]
                q.append(nx)
    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    board = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        board[a].append(b)
        board[b].append(a)
    visited = [0] * (v + 1)
    for i in range(v):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                break
    else:
        print("YES")

# https://www.acmicpc.net/problem/2644
import sys
from collections import deque, defaultdict


def dfs(cur):
    if visited[b] != -1:
        return
    for ncur in board[cur]:
        if visited[ncur] == -1:
            visited[ncur] = visited[cur] + 1
            dfs(ncur)


def bfs():
    q = deque()
    q.append(a)
    while q:
        cur = q.popleft()
        for ncur in board[cur]:
            if visited[ncur] == -1:
                q.append(ncur)
                visited[ncur] = visited[cur] + 1


input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
board=defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)

visited = [-1] * (n + 1)
visited[a] = 0
# bfs()
dfs(a)
print(visited[b])

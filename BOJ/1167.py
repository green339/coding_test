# https://www.acmicpc.net/problem/1167
from collections import deque


def bfs(start, flag):
    visited = [-1] * (V + 1)
    q = deque()
    q.append(start)
    visited[start] = 0
    answer = [0, 0]
    while q:
        x = q.popleft()
        for nx, l in board[x]:
            if visited[nx] == -1:
                visited[nx] = visited[x] + l
                q.append(nx)
                if visited[nx] > answer[0]:
                    answer = [visited[nx], nx]
    return answer[flag]


V = int(input())
board = dict()
for _ in range(V):
    tmp = deque(map(int, input().split()))
    s = tmp.popleft()
    board[s] = []
    while tmp[0] != -1:
        e = tmp.popleft()
        c = tmp.popleft()
        board[s].append((e, c))

print(bfs(bfs(1, 1), 0))

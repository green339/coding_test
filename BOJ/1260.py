import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def dfs(x, visited):
    visited.append(x)
    for nx in board.get(x, []):
        if nx not in visited:
            visited = dfs(nx, visited)
    return visited


def bfs(start):
    q = deque([start])
    visited = [start]
    while q:
        x = q.popleft()
        for nx in board.get(x, []):
            if nx not in visited:
                visited.append(nx)
                q.append(nx)
    return visited


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    global board
    board = defaultdict(list)
    for _ in range(M):
        s, e = map(int, input().split())
        board[s].append(e)
        board[e].append(s)
    board = dict(map(lambda x: (x[0], sorted(x[1])), board.items()))
    print(*dfs(V, []))
    print(*bfs(V))

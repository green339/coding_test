# https://www.acmicpc.net/problem/11724
import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        vx = q.popleft()
        for nx in graph[vx]:
            if nx not in visited:
                visited.add(nx)
                q.append(nx)


if __name__ == "__main__":
    global graph
    graph = defaultdict(set)
    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)
    global visited
    visited = set()
    ans = 0
    for i in range(1,N+1):
        if i not in visited:
            visited.add(i)
            bfs(i)
            ans += 1
    print(ans)

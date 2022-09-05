# https://www.acmicpc.net/problem/1238
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
INF = sys.maxsize


N, M, X = map(int, input().split())
board = defaultdict(list)
for _ in range(M):
    s, e, t = map(int, input().split())
    board[s].append((e, t))


def dijkstra(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for v, time in board[cur]:
            tmp = time + cost
            if dist[v] > tmp:
                dist[v] = tmp
                heapq.heappush(q, (tmp, v))
    return dist


back = dijkstra(X)
answer = 0
for i in range(1, N + 1):
    answer = max(answer, back[i] + dijkstra(i)[X])
print(answer)

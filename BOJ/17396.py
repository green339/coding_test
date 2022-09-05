# https://www.acmicpc.net/problem/17396
import sys
from collections import defaultdict
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())
visible = list(map(int, input().split()))
visible[-1] = 0
board = defaultdict(list)
for _ in range(M):
    a, b, t = map(int, input().split())
    board[a].append((b, t))
    board[b].append((a, t))
dist = [INF] * N
dist[0] = 0
q = []
heapq.heappush(q, (0, 0))  # cost, cur
while q:
    cost, cur = heapq.heappop(q)
    if dist[cur] < cost:
        continue
    for i, t in board[cur]:
        tmp = cost + t
        if dist[i] > tmp and not visible[cur]:
            dist[i] = tmp
            heapq.heappush(q, (tmp, i))
print(dist[-1] if dist[-1] < INF else -1)

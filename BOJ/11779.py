# https://www.acmicpc.net/problem/11779
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
board = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    board[s].append((e, c))
a, b = map(int, input().split())
dist = [INF] * (n + 1)
prior = [0] * (n + 1)  # 이전에 거쳐서 가는 점
dist[a] = 0
q = []
heapq.heappush(q, (0, a))
while q:
    cost, cur = heapq.heappop(q)
    if cur == b:
        break
    if dist[cur] < cost:
        continue
    for bi, bc in board[cur]:
        tmp = cost + bc
        if dist[bi] > tmp:
            dist[bi] = tmp
            prior[bi] = cur
            heapq.heappush(q, (tmp, bi))
route = [b]
while prior[route[-1]]:
    route.append(prior[route[-1]])
print(dist[b])
print(len(route))
print(*route[::-1])

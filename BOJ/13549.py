# https://www.acmicpc.net/problem/13549
import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
q = []
heapq.heappush(q, (0, N))
visited = [0] * 100001
visited[N] = 1
while q:
    cnt, x = heapq.heappop(q)
    if x == K:
        print(cnt)
        break
    if 0 <= x + x < 100001 and not visited[x + x]:
        visited[x + x] = 1
        heapq.heappush(q, (cnt, x + x))
    if 0 <= x + 1 < 100001 and not visited[x + 1]:
        visited[x + 1] = 1
        heapq.heappush(q, (cnt + 1, x + 1))
    if 0 <= x - 1 < 100001 and not visited[x - 1]:
        visited[x - 1] = 1
        heapq.heappush(q, (cnt + 1, x - 1))

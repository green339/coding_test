# https://www.acmicpc.net/problem/11657
from collections import defaultdict

N, M = map(int, input().split())
bus = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    bus[A].append((B, C))

dist = [1e9] * (N + 1)
dist[1] = 0
# 도시의 수만큼 반복
# N-1번 까지는 최소 거리 찾기 -> 각 정점의 최단 거리는 최대 N-1개의 정점을 거쳐서 만들 수 있다.
# N번 째는 음의 사이클 찾기)

for k in range(N):
    for i in bus.keys():
        for j, c in bus[i]:
            if dist[i] != 1e9 and dist[j] > c + dist[i]:
                dist[j] = dist[i] + c
                if k == N - 1:
                    print(-1)
                    break
        else:
            continue
        break
    else:
        continue
    break
else:
    for dest in range(2, N+1):
        if dist[dest] == 1e9:
            print(-1)
        else:
            print(dist[dest])

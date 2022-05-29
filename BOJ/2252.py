# https://www.acmicpc.net/problem/2252
from collections import defaultdict, deque
import sys

input = sys.stdin.readline
order = defaultdict(list)
indegree = defaultdict(int)
N, M = map(int, input().split())
for _ in range(M):
    A, B = map(int, input().split())
    order[A].append(B)
    indegree[B] += 1
q = deque()
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)
answer = []
while q:
    pre_node = q.popleft()
    answer.append(pre_node)
    for post_node in order[pre_node]:
        indegree[post_node] -= 1
        if not indegree[post_node]:
            q.append(post_node)
print(*answer)

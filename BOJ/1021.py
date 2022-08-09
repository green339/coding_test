# https://www.acmicpc.net/problem/1021
from collections import deque

N, M = map(int, input().split())
pick = list(map(int, input().split()))
q = deque(i for i in range(1, N + 1))
answer = 0
for p in pick:
    idx = q.index(p)
    if idx <= len(q) // 2:
        q.rotate(-idx)
        answer += idx
    else:
        q.rotate(len(q) - idx)
        answer += len(q) - idx
    q.popleft()
print(answer)

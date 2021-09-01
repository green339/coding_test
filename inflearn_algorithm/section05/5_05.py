import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque(i for i in range(1, N + 1))
cnt = 1
while len(q) > 1:
    prince = q.popleft()
    if cnt == K:
        cnt = 1
    else:
        q.append(prince)
        cnt += 1
print(q.pop())

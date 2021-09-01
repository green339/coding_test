import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
waiting = deque((pos, danger) for pos, danger in enumerate(list(map(int, sys.stdin.readline().split()))))
cnt = 0
while True:
    n, d = waiting.popleft()
    if any(d < y for x, y in waiting):
        waiting.append((n, d))
    else:
        cnt += 1
        if n == M:
            break
print(cnt)

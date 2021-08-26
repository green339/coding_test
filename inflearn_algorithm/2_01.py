import sys

p, k = map(int, sys.stdin.readline().split())
q = []
for i in range(1, p + 1):
    if not p % i:
        q.append(i)
if len(q) < k:
    print(-1)
else:
    print(q[k - 1])

# https://www.acmicpc.net/problem/17140
import sys
from collections import defaultdict

input = sys.stdin.readline


def sort_operation(arr):
    res = []
    cnt = defaultdict(int)
    for row in arr:
        if not row:
            continue
        cnt[row] += 1
    for key, value in sorted(cnt.items(), key=lambda x: (x[1], x[0])):
        res.append(key)
        res.append(value)
    return res


def rc_operation(arr):
    res = []
    max_len = 0
    for row in arr:
        res.append(sort_operation(row))
        max_len = max(max_len, len(res[-1]))
    for i in range(len(res)):
        for j in range(len(res[i]), max_len):
            res[i].append(0)
    return res


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
t = 0
while t <= 101:
    if len(A) >= r and len(A[0]) >= c and A[r - 1][c - 1] == k:
        break
    if len(A) >= len(A[0]):
        A = rc_operation(A)
    else:
        A = rc_operation(list(zip(*A)))
        A = list(zip(*A))
    t += 1
print(t if t <= 100 else -1)

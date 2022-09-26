# https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
answer = []
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 1:
        if find(a) == find(b):
            answer.append("YES")
        else:
            answer.append("NO")
    else:
        union(a, b)

for a in answer:
    print(a)

# https://www.acmicpc.net/problem/1717
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])  # 부모 노드의 부모 노드 찾기
    return parent[node]


def union(parent,x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x < y:
        parent[y] = parent[x]
    else:
        parent[x] = parent[y]


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
ans = []
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 1:
        if find(a) == find(b):
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        union(parent,a, b)
for a in ans:
    print(a)

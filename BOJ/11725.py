# https://www.acmicpc.net/problem/11725
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(start, visited):
    visited.add(start)
    for i in link.get(start, []):
        if i not in visited:
            tree[i] = start
            dfs(i, visited)


if __name__ == "__main__":
    N = int(input())
    global link
    link = defaultdict(list)
    global tree
    tree = [0] * (N + 1)
    for _ in range(N - 1):
        s, e = map(int, input().split())
        link[s].append(e)
        link[e].append(s)
    dfs(1, set())
    for idx in range(2,N+1):
        print(tree[idx])

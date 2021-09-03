import sys


def dfs(d, s):
    global ans
    if s > C:
        return
    if s + sum([i for i in range(d, N)]) < ans:
        return
    if d == N:
        if s <= C:
            ans = max(ans, s)
    else:
        dfs(d + 1, dogs[d] + s)
        dfs(d + 1, s)


C, N = map(int, sys.stdin.readline().split())
dogs = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
dfs(0, 0)
print(ans)

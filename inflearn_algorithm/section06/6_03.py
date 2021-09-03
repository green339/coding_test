import sys


def dfs(d):
    if d == N + 1:
        ans = [i for i in range(1, N + 1) if num[i]]
        print(*ans)
    else:
        num[d] = 1
        dfs(d + 1)
        num[d] = 0
        dfs(d + 1)


N = int(sys.stdin.readline())
num = [0] * (N + 1)
dfs(1)

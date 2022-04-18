# https://www.acmicpc.net/problem/14888
import sys

input = sys.stdin.readline
max_ans = -1e9
min_ans = 1e9


def dfs(depth, temp):
    global max_ans, min_ans
    if depth == N:
        max_ans = max(temp, max_ans)
        min_ans = min(temp, min_ans)
        return
    for i in range(4):
        if op[i]:
            op[i] -= 1
            if i == 0:
                dfs(depth + 1, temp + A[depth])
            elif i == 1:
                dfs(depth + 1, temp - A[depth])
            elif i == 2:
                dfs(depth + 1, temp * A[depth])
            elif i == 3:
                dfs(depth + 1, int(temp / A[depth]))
            op[i] += 1


N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
dfs(1, A[0])
print(max_ans)
print(min_ans)

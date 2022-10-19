# https://www.acmicpc.net/problem/14501

import sys

input = sys.stdin.readline

N = int(input())
plan = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
for i in range(1, N + 1):
    if plan[i][0] + i - 1 <= N:
        dp[plan[i][0] + i - 1] = max(dp[plan[i][0] + i - 1], dp[i - 1] + plan[i][1])
    dp[i] = max(dp[i], dp[i - 1])
print(dp[-1])

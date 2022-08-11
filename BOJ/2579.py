# https://www.acmicpc.net/problem/2579
import sys

input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]
if n == 1:
    print(stairs[-1])
else:
    dp = [0] * (n + 1)
    dp[1] = stairs[0]
    dp[2] = stairs[0] + stairs[1]
    for i in range(3, n + 1):
        dp[i] = max(stairs[i - 2] + dp[i - 3], dp[i - 2]) + stairs[i - 1]
    print(dp[-1])

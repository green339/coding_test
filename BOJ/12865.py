# https://www.acmicpc.net/problem/12865
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)
weight = 0
for i in range(0, N):
    w, v = bag[i]
    for j in range(K, w - 1, -1): # 끝부터 해보는 것
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[-1])

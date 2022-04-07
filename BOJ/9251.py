# https://www.acmicpc.net/problem/9251
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    x = input().strip()
    y = input().strip()
    n = len(x)
    m = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[j][i] = dp[j - 1][i - 1] + 1
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j - 1][i])
    print(dp[-1][-1])

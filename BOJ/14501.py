# https://www.acmicpc.net/problem/14501
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    plan = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (N + 1)
    for d in range(1, N + 1):
        t, p = plan[d - 1]
        finish = d + t - 1
        if finish < N + 1:
            dp[finish] = max(dp[finish], dp[d - 1] + p)
        dp[d] = max(dp[d], dp[d - 1])

    print(dp[-1])

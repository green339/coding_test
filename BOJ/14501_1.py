# https://www.acmicpc.net/problem/14501
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    plan = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (N + 1)  # i 번째 날에 끝나는 일, 받을 수 있는 최대값
    for i in range(1, N + 1):
        t, p = plan[i - 1]
        finish = i + t - 1
        if finish <= N:  # 끝나는 날 최대값 찾기
            dp[finish] = max(dp[finish], dp[i - 1] + p)
        dp[i] = max(dp[i - 1], dp[i])  # 이전 날까지 한 것과 최대 비교
    print(dp[-1])

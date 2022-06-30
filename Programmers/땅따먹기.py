# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    for j in range(4):
        dp[0][j] = land[0][j]
    for i in range(n - 1):
        dp[i + 1][0] = land[i + 1][0] + max(dp[i][1], dp[i][2], dp[i][3])
        dp[i + 1][1] = land[i + 1][1] + max(dp[i][0], dp[i][2], dp[i][3])
        dp[i + 1][2] = land[i + 1][2] + max(dp[i][0], dp[i][1], dp[i][3])
        dp[i + 1][3] = land[i + 1][3] + max(dp[i][0], dp[i][1], dp[i][2])
    return max(dp[-1])

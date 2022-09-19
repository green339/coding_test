# https://www.acmicpc.net/problem/9252
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    x = input().strip()
    y = input().strip()
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(dp[-1][-1])
    cur = dp[-1][-1]
    answer = []
    a, b = m, n
    while dp[a][b]:
        if dp[a][b] - 1 == dp[a - 1][b] and dp[a][b] - 1 == dp[a][b - 1]:
            answer.append(x[a - 1])
            a -= 1
            b -= 1
        else:
            if dp[a - 1][b] > dp[a][b - 1]:
                a -= 1
            else:
                b -= 1
    if answer:
        print(''.join(reversed(answer)))

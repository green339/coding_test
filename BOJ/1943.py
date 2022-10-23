# https://www.acmicpc.net/problem/1943
import sys

input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coin = [list(map(int, input().split())) for _ in range(N)]
    target = sum([a * b for a, b in coin])
    answer = 0
    if target % 2:
        print(0)
        continue
    target //= 2
    dp = [1] + [0] * target
    for cost, cnt in coin:
        for money in range(target, cost - 1, -1):
            if dp[money - cost]:
                for c in range(cnt):
                    if money + cost * c > target:
                        continue
                    dp[money + cost * c] = 1
    print(dp[target])

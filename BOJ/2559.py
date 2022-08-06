# https://www.acmicpc.net/problem/2559
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))
cur = sum(temperature[:k])
answer = cur
for i in range(k, n):
    cur = cur - temperature[i - k] + temperature[i]
    answer = max(answer, cur)
print(answer)

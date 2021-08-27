import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
dice = defaultdict(int)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dice[i + j] += 1
temp = sorted(dice.items(), reverse=True, key=lambda x: x[1])
for j in temp:
    if temp[0][1] == j[1]:
        print(j[0], end=' ')
    else:
        break

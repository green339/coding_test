# https://www.acmicpc.net/problem/13458
import sys
import math
input = sys.stdin.readline

N = int(input())
A = map(int, input().split())
B, C = map(int, input().split())
answer = 0
for ai in A:
    answer += 1 + math.ceil(max(0, (ai - B)) / C)
print(answer)

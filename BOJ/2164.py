# https://www.acmicpc.net/problem/2164
import sys

input = sys.stdin.readline

N = int(input())
q = [i for i in range(1, N + 1)]
l = len(q)
while l > 1:
    if l % 2:
        q = [q[-1]] + q[1:l:2]
    else:
        q = q[1:l:2]
    l = len(q)
print(q[0])

# https://www.acmicpc.net/problem/11723
import sys

input = sys.stdin.readline

M = int(input())
s = [0] * 21
for _ in range(M):
    op = input().split()
    if len(op) > 1:
        op[1] = int(op[1])
    if op[0] == "add":
        s[op[1]] = 1
    elif op[0] == "remove":
        s[op[1]] = 0
    elif op[0] == "check":
        print(s[op[1]])
    elif op[0] == "toggle":
        s[op[1]] = int(not s[op[1]])
    elif op[0] == "all":
        s = [1] * 21
    elif op[0] == "empty":
        s = [0] * 21

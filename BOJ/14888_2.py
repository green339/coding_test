# https://www.acmicpc.net/problem/14888
import sys

input = sys.stdin.readline


def dfs(depth, cur):
    global max_answer, min_answer
    if depth == N:
        max_answer = max(max_answer, cur)
        min_answer = min(min_answer, cur)
        return
    if op[0]:
        op[0] -= 1
        dfs(depth+1, cur + A[depth])
        op[0] += 1
    if op[1]:
        op[1] -= 1
        dfs(depth+1, cur - A[depth])
        op[1] += 1
    if op[2]:
        op[2] -= 1
        dfs(depth+1, cur * A[depth])
        op[2] += 1
    if op[3]:
        op[3] -= 1
        dfs(depth+1, int(cur / A[depth]))
        op[3] += 1


N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
max_answer = -10e13
min_answer = 10e13
dfs(1, A[0])
print(max_answer)
print(min_answer)

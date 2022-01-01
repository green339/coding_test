# https://www.acmicpc.net/problem/14888
import sys
from itertools import permutations

input = sys.stdin.readline


# 브루트포스
def perm():
    global min_ans, max_ans
    for p in set(permutations(operator)):
        result = int(A[0])
        for k in range(1, N):
            if p[k - 1] == "+":
                result += A[k]
            elif p[k - 1] == "-":
                result -= A[k]
            elif p[k - 1] == "*":
                result *= A[k]
            elif p[k - 1] == "/":
                result = int(result / A[k])
        min_ans = min(min_ans, result)
        max_ans = max(max_ans, result)


# dfs
def dfs(depth, op, result):
    global min_ans, max_ans
    if depth == N:
        min_ans = min(min_ans, result)
        max_ans = max(max_ans, result)
        return
    else:
        if op[0]:
            op[0] -= 1
            dfs(depth + 1, op, result + A[depth])
            op[0] += 1
        if op[1]:
            op[1] -= 1
            dfs(depth + 1, op, result - A[depth])
            op[1] += 1
        if op[2]:
            op[2] -= 1
            dfs(depth + 1, op, result * A[depth])
            op[2] += 1
        if op[3]:
            op[3] -= 1
            dfs(depth + 1, op, int(result / A[depth]))
            op[3] += 1


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    min_ans = 10e9
    max_ans = -10e9
    operator = []
    for i, o in enumerate(["+", "-", "*", "/"]):
        operator.extend(o * B[i])
    perm()  # 방법1
    dfs(1, B, A[0])  # 방법2
    print(max_ans)
    print(min_ans)

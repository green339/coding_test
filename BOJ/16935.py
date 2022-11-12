# https://www.acmicpc.net/problem/16935
import sys
from copy import deepcopy

input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
op = list(map(int, input().split()))
n = N // 2
m = M // 2
for o in op:
    if o == 1:
        A = A[::-1]
    elif o == 2:
        A = [arr[::-1] for arr in A]
    elif o == 3:
        A = list(arr[::-1] for arr in map(list, zip(*A)))
        N = len(A)
        M = len(A[0])
        n = N // 2
        m = M // 2
    elif o == 4:
        A = list(map(list, zip(*A)))[::-1]
        N = len(A)
        M = len(A[0])
        n = N // 2
        m = M // 2
    elif o == 5:
        tmp = [[0] * M for _ in range(N)]
        for i in range(n):
            for j in range(m):
                tmp[i][j + m] = A[i][j]
                tmp[i][j] = A[i + n][j]
                tmp[i + n][j] = A[i + n][j + m]
                tmp[i + n][j + m] = A[i][j + m]
        A = deepcopy(tmp)
    elif o == 6:
        tmp = [[0] * M for _ in range(N)]
        for i in range(n):
            for j in range(m):
                tmp[i + n][j] = A[i][j]
                tmp[i][j] = A[i][j + m]
                tmp[i][j + m] = A[i + n][j + m]
                tmp[i + n][j + m] = A[i + n][j]
        A = deepcopy(tmp)
for a in A:
    print(*a)

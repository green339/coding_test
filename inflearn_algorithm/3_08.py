import sys
from collections import deque

N = int(sys.stdin.readline())
board = [deque(map(int, sys.stdin.readline().split())) for _ in range(N)]
M = int(sys.stdin.readline())
case = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
for r, d, c in case:
    if d:
        board[r - 1].rotate(c)
    else:
        board[r - 1].rotate(-c)
mid = N // 2
total = board[mid][mid]
for i in range(mid):
    s = i
    e = N - i
    for j in range(s, e):
        total += (board[i][j] + board[N - 1 - i][j])
print(total)

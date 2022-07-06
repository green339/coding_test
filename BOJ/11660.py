# https://www.acmicpc.net/problem/11660
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        board[i][j] = board[i][j - 1] + board[i - 1][j] - board[i - 1][j - 1] + arr[i - 1][j - 1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])

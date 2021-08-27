import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
mid = N // 2
total = sum(board[mid])
for i in range(N // 2):
    s = mid - i
    e = mid + i + 1
    total += (sum(board[N - 1 - i][s:e]) + sum(board[i][s:e]))
print(total)

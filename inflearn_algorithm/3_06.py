import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
c1 = 0
c2 = 0
for i,b in enumerate(zip(*board)):
    ans = max(sum(b), ans, sum(board[i]))
    c1 += board[i][i]
    c2 += board[N - 1 - i][N - 1 - i]
ans = max(c1, c2, ans)
print(ans)

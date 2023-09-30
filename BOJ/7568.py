# https://www.acmicpc.net/problem/7568
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = [1] * N
for i in range(N):
    for j in range(i + 1, N):
        if board[i][0] > board[j][0] and board[i][1] > board[j][1]:
            ans[j] += 1
        elif board[i][0] < board[j][0] and board[i][1] < board[j][1]:
            ans[i] += 1

print(*ans)

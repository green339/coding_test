# https://www.acmicpc.net/problem/14500
import sys

input = sys.stdin.readline


def dfs(cur, depth, x, y):
    global answer
    if depth == 3:
        answer = max(answer, cur)
        return
    for dx, dy in d:
        nx = dx + x
        ny = dy + y
        if -1 < nx < N and -1 < ny < M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(cur + board[nx][ny], depth + 1, nx, ny)
            visited[nx][ny] = 0


def middle(x, y):
    global answer
    surround = [-1, -1, -1, -1]
    if x - 1 > -1:
        surround[0] = board[x - 1][y]
    if x + 1 < N:
        surround[1] = board[x + 1][y]
    if y - 1 > -1:
        surround[2] = board[x][y - 1]
    if y + 1 < M:
        surround[3] = board[x][y + 1]
    answer = max(answer, board[x][y] + sum(surround) - min(surround))


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(board[r][c], 0, r, c)
        visited[r][c] = 0
        middle(r, c)
print(answer)

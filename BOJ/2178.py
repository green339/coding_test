# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(N)]
    q = deque()
    q.append((0, 0))
    board[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == M - 1:
            break
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                    board[nx][ny] += board[x][y]
    print(board[N - 1][M - 1])

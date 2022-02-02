# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

if __name__ == "__main__":
    M, N = map(int, input().split())
    board = []
    start = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j, b in enumerate(board[-1]):
            if b == 1:
                start.append((1, i, j))
    q = deque(start)
    t = 1
    while q:
        t, x, y = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] == 0:
                    board[nx][ny] = t
                    q.append((t + 1, nx, ny))
    answer = t - 1
    for r in range(N):
        for c in range(M):
            if not board[r][c]:
                answer = -1
    print(answer)

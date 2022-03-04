# https://www.acmicpc.net/problem/1012
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        vx, vy = q.popleft()
        for dx, dy in d:
            nx = vx + dx
            ny = vy + dy
            if -1 < nx < N and -1 < ny < M and board[nx][ny]:
                board[nx][ny] = 0
                q.append((nx, ny))


if __name__ == "__main__":
    global board, M, N
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        board = [[0] * M for _ in range(N)]
        for _ in range(K):
            ky, kx = map(int, input().split())
            board[kx][ky] = 1
        ans = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    bfs(i, j)
                    ans += 1
        print(ans)

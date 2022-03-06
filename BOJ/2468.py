# https://www.acmicpc.net/problem/11724
import sys
from collections import deque

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y, s):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        vx, vy = q.popleft()
        for dx, dy in d:
            nx = vx + dx
            ny = vy + dy
            if -1 < nx < N and -1 < ny < N:
                if board[nx][ny] >= s and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    a = min(map(min, board))
    b = max(map(max, board))
    ans = 0
    for k in range(a, b + 1):
        global visited
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] >= k and not visited[i][j]:
                    visited[i][j] = 1
                    cnt += bfs(i, j, k)
        ans = max(cnt, ans)
    print(ans)

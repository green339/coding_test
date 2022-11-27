# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def move(sx, sy):
    q = deque()
    q.append((sx, sy))
    union = set()
    union.add((sx, sy))
    ppl = board[sx][sy]
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if -1 < nx < n and -1 < ny < n:
                if (nx, ny) not in union and not visited[nx][ny]:
                    if l <= abs(board[x][y] - board[nx][ny]) <= r:
                        union.add((nx, ny))
                        q.append((nx, ny))
                        ppl += board[nx][ny]
    if len(union) == 1:
        return 0
    ppl //= len(union)
    for ux, uy in union:
        board[ux][uy] = ppl
        visited[ux][uy] = 1
    return 1


n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(i % 2, n, 2): # 상하좌우로 탐색하니까 이미 탐색한 곳은 탐색 X되도록 (격자로)
            if not visited[i][j]:
                flag |= move(i, j)
    answer += flag
    if not flag:
        print(answer)
        break

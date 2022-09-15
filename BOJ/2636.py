# https://www.acmicpc.net/problem/2636
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    cnt = 0
    board[0][0] = t
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < r and -1 < ny < c and board[nx][ny] > t:
                if board[nx][ny] == 1:
                    board[nx][ny] = t
                    cnt += 1
                else:
                    board[nx][ny] = t
                    q.append((nx, ny))
    return cnt


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
zeros = sum([b.count(0) for b in board])
answer = 0
t = 0
while zeros < r * c:
    t -= 1
    answer = bfs()
    zeros += answer
print(-t)
print(answer)



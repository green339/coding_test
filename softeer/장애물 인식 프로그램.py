# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=409
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
answer = []
for x in range(n):
    for y in range(n):
        if board[x][y]:
            q = deque()
            q.append([x, y])
            board[x][y] = 0
            cnt = 0
            while q:
                nx, ny = q.popleft()
                cnt += 1
                for i in range(4):
                    vx = nx + dx[i]
                    vy = ny + dy[i]
                    if -1 < vx < n and -1 < vy < n:
                        if board[vx][vy]:
                            board[vx][vy] = 0
                            q.append([vx, vy])
            answer.append(cnt)

print(len(answer))
for ans in sorted(answer):
    print(ans)
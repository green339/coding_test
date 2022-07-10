# https://www.acmicpc.net/problem/2667
import sys
from collections import deque

input = sys.stdin.readline
di = [-1, 0, 0, 1]
dj = [0, 1, -1, 0]

N = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
answer = []
for x in range(N):
    for y in range(N):
        if board[x][y]:
            board[x][y] = 0
            cnt = 1
            q = deque()
            q.append((x, y))
            while q:
                i, j = q.popleft()
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if -1 < ni < N and -1 < nj < N:
                        if board[ni][nj]:
                            cnt += 1
                            q.append((ni, nj))
                            board[ni][nj] = 0
            answer.append(cnt)
print(len(answer))
for a in sorted(answer):
    print(a)

# https://www.acmicpc.net/problem/13460
import sys
from collections import deque


def move(loc, dx, dy):
    result = []
    for x, y, c in loc:
        while True:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] == 'O':  # 구슬이 구멍에 빠지는지
                    result.append((nx, ny, c))
                    break
                elif result and nx == result[0][0] and ny == result[0][1]:  # 앞서간 값이랑 같은 위치인지
                    result.append((x, y, c))
                    break
                elif board[nx][ny] == '#':
                    result.append((x, y, c))
                    break
                else:
                    x = nx
                    y = ny
    result.sort()
    if tuple(result) in visited:
        return []
    else:
        visited.add(tuple(result))
        return result


d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
marble = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            marble.append((i, j, 'R'))
        elif board[i][j] == 'B':
            marble.append((i, j, 'B'))

q = deque()
q.append((0, marble))
visited = set()
while q:
    cnt, cur = q.popleft()
    cur.sort(key=lambda x: x[-1])
    if board[cur[0][0]][cur[0][1]] == 'O':
        continue
    if board[cur[-1][0]][cur[-1][1]] == 'O':
        print(cnt)
        break
    if cnt > 10:
        print(-1)
        break
    for di, dj in d:
        if di:  # x축 방향으로 움직이는 경우
            cur.sort(key=lambda x: (-x[0] * di))
        else:  # y축 방향으로 움직이는 경우
            cur.sort(key=lambda x: (-x[1] * dj))
        res = move(cur, di, dj)
        if res:
            q.append((cnt + 1, res))
else:
    print(-1)

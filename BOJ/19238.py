# https://www.acmicpc.net/problem/19238ㅋ
import sys
from collections import deque

input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def find_passenger(sx, sy):
    global fuel
    res = []
    if board[sx][sy] > 1:
        res.append((sx, sy))
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if res and visited[x][y] >= visited[res[0][0]][res[0][1]]:
            continue
        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if -1 < nx < N and -1 < ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    if board[nx][ny] == 1:
                        continue
                    if board[nx][ny] > 1:
                        res.append((nx, ny))
                    q.append((nx, ny))
    if not res:
        return []
    res.sort()
    if visited[res[0][0]][res[0][1]] - 1 < fuel:
        fuel -= (visited[res[0][0]][res[0][1]] - 1)
        return res[0]
    else:
        return []


def move(sx, sy):
    global fuel
    cur = board[sx][sy]  # 현재 승객번호
    board[sx][sy] = 0
    dest = passenger[cur]
    if (sx, sy) == dest:
        return cur
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if (x, y) == dest:
            continue
        for dx, dy in direction:
            nx = dx + x
            ny = dy + y
            if -1 < nx < N and -1 < ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    if board[nx][ny] == 1:
                        continue
                    q.append((nx, ny))
    if not visited[dest[0]][dest[1]]:
        return 0
    if visited[dest[0]][dest[1]] - 1 <= fuel:
        fuel += (visited[dest[0]][dest[1]] - 1)
        return cur
    else:
        return 0


N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
taxi_x, taxi_y = map(int, input().split())
taxi_x -= 1
taxi_y -= 1
passenger = dict()
for p in range(2, M + 2):
    a, b, c, d = map(int, input().split())
    passenger[p] = (c - 1, d - 1)
    board[a - 1][b - 1] = p
finish = set()
while len(finish) != M:
    p = find_passenger(taxi_x, taxi_y)
    if not p:
        break
    pn = move(p[0], p[1])
    if not pn:
        break
    finish.add(pn)
    taxi_x, taxi_y = passenger[pn]
print(fuel if len(finish) == M else -1)

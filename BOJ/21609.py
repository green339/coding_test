# https://www.acmicpc.net/problem/21609
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def block_count(sx, sy):
    rainbow = set()
    flag = False
    global block_size
    global rainbow_block
    q = deque()
    q.append((sx, sy))
    block_cnt = 1
    rainbow_cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < N and not visited[nx][ny]:
                if board[nx][ny] == color:
                    visited[nx][ny] = 1
                    block_cnt += 1
                    q.append((nx, ny))
                elif not board[nx][ny] and (nx, ny) not in rainbow:
                    rainbow.add((nx, ny))
                    block_cnt += 1
                    rainbow_cnt += 1
                    q.append((nx, ny))
    if block_cnt > block_size:
        block_size = block_cnt
        rainbow_block = rainbow_cnt
        flag = True
    elif block_cnt == block_size and rainbow_cnt >= rainbow_block:
        rainbow_block = rainbow_cnt
        flag = True
    return flag


def erase():
    q = deque()
    q.append((bx, by))
    c = board[bx][by]
    board[bx][by] = -2
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < N:
                if board[nx][ny] == c or not board[nx][ny]:
                    q.append((nx, ny))
                    board[nx][ny] = -2


def gravity():
    for y in range(N):
        floor = N
        for x in range(N - 1, -1, -1):
            if board[x][y] == -2:
                continue
            elif board[x][y] == -1:
                floor = x
            else:
                board[floor - 1][y] = board[x][y]
                if floor - 1 != x:
                    board[x][y] = -2
                floor -= 1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    visited = [[0] * N for _ in range(N)]
    block_size = 0
    rainbow_block = 0
    bx, by = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or board[i][j] < 1:
                continue
            visited[i][j] = 1
            color = board[i][j]
            if block_count(i, j):
                bx, by = i, j
    if block_size < 2:
        break
    erase()
    answer += block_size ** 2
    gravity()
    board = list(map(list, list(zip(*board))[::-1]))
    gravity()

print(answer)

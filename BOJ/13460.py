# https://www.acmicpc.net/problem/13460
from collections import deque

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move(color):
    global pnrx, pnry, pnbx, pnby
    goal = False
    if color == 'R':
        nrx = rx
        nry = ry
        while True:
            nrx += dx
            nry += dy
            if board[nrx][nry] == '.' and not (nrx == pnbx and nry == pnby):
                pnrx = nrx
                pnry = nry
            elif board[nrx][nry] == 'O':
                goal = True
                pnrx = 0
                pnry = 0
                break
            else:
                break
        red.append((rm + 1, pnrx, pnry))
    elif color == 'B':
        nbx = bx
        nby = by
        while True:
            nbx += dx
            nby += dy
            if board[nbx][nby] == '.' and not (nbx == pnrx and nby == pnry):
                pnbx = nbx
                pnby = nby
            elif board[nbx][nby] == 'O':
                goal = True
                pnbx = 0
                pnby = 0
                break
            else:
                break
        blue.append((bm + 1, pnbx, pnby))
    return goal


N, M = map(int, input().split())
board = []
blue = deque()
red = deque()
for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[-1][j] == 'B':
            blue.append((0, i, j))
            board[i][j] = '.'
        elif board[-1][j] == 'R':
            red.append((0, i, j))
            board[i][j] = '.'
while True:
    rm, rx, ry = red.popleft()
    bm, bx, by = blue.popleft()
    if not rx or not bx:  # 이전에 골을 한 경우
        continue
    if rm == 10:
        break
    result = []
    for dx, dy in d:
        # 어떤 공을 먼저 움직일지 정한다.
        pnrx = rx
        pnry = ry
        pnbx = bx
        pnby = by
        if dx == 1:
            if rx < bx:
                # 파 부터
                bc = move('B')
                rc = move('R')
            else:
                # 빨 부터
                rc = move('R')
                bc = move('B')
        elif dx == -1:
            if rx > bx:
                # 파 부터
                bc = move('B')
                rc = move('R')
            else:
                # 빨 부터
                rc = move('R')
                bc = move('B')
        elif dy == 1:
            if ry < by:
                # 파 부터
                bc = move('B')
                rc = move('R')
            else:
                # 빨 부터
                rc = move('R')
                bc = move('B')
        elif dy == -1:
            if ry > by:
                # 파 부터
                bc = move('B')
                rc = move('R')
            else:
                # 빨 부터
                rc = move('R')
                bc = move('B')
        result.append((rc, bc))
    # result 보고 결정
    win = set()
    for a, b in result:
        if b == 1:
            win.add('B')
        elif a == 1:
            win.add('R')
    if 'R' in win:
        break
if rm == 10 or 'R' not in win:
    print(-1)
else:
    print(rm + 1)

# bfs로 다시 풀기

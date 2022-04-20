# https://www.acmicpc.net/problem/15683
def up(x, y, s):
    while -1 < x:
        if board[x][y] == 6:
            break
        if 0 < board[x][y] < 6:
            x -= 1
            continue
        board[x][y] += s
        x -= 1


def down(x, y, s):
    while x < N:
        if board[x][y] == 6:
            break
        if 0 < board[x][y] < 6:
            x += 1
            continue
        board[x][y] += s
        x += 1


def left(x, y, s):
    while -1 < y:
        if board[x][y] == 6:
            break
        if 0 < board[x][y] < 6:
            y -= 1
            continue
        board[x][y] += s
        y -= 1


def right(x, y, s):
    while y < M:
        if board[x][y] == 6:
            break
        if 0 < board[x][y] < 6:
            y += 1
            continue
        board[x][y] += s
        y += 1


def blind_spot_cnt():
    global answer
    cnt = 0
    for b in board:
        cnt += b.count(0)
    answer = min(cnt, answer)


def dfs(depth):
    if depth == watcher_cnt:
        blind_spot_cnt()
        return
    x, y = watcher[depth]
    if board[x][y] == 1:
        left(x, y, -1)
        dfs(depth + 1)
        left(x, y, 1)

        right(x, y, -1)
        dfs(depth + 1)
        right(x, y, 1)

        down(x, y, -1)
        dfs(depth + 1)
        down(x, y, 1)

        up(x, y, -1)
        dfs(depth + 1)
        up(x, y, 1)

    elif board[x][y] == 2:
        left(x, y, -1)
        right(x, y, -1)
        dfs(depth + 1)
        left(x, y, 1)
        right(x, y, 1)
        down(x, y, -1)
        up(x, y, -1)
        dfs(depth + 1)
        down(x, y, 1)
        up(x, y, 1)

    elif board[x][y] == 3:
        up(x, y, -1)
        right(x, y, -1)
        dfs(depth + 1)
        up(x, y, 1)

        down(x, y, -1)
        dfs(depth + 1)
        right(x, y, 1)

        left(x, y, -1)
        dfs(depth + 1)
        down(x, y, 1)

        up(x, y, -1)
        dfs(depth + 1)
        up(x, y, 1)
        left(x, y, 1)

    elif board[x][y] == 4:
        left(x, y, -1)
        down(x, y, -1)
        up(x, y, -1)
        dfs(depth + 1)
        left(x, y, 1)

        right(x, y, -1)
        dfs(depth + 1)
        up(x, y, 1)

        left(x, y, -1)
        dfs(depth + 1)
        down(x, y, 1)

        up(x, y, -1)
        dfs(depth + 1)
        left(x, y, 1)
        right(x, y, 1)
        up(x, y, 1)

    elif board[x][y] == 5:
        left(x, y, -1)
        right(x, y, -1)
        down(x, y, -1)
        up(x, y, -1)
        dfs(depth + 1)
        left(x, y, 1)
        right(x, y, 1)
        down(x, y, 1)
        up(x, y, 1)


N, M = map(int, input().split())
board = []
watcher = []
watcher_cnt = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if 0 < board[-1][j] < 6:
            watcher.append([i, j])
            watcher_cnt += 1
answer = N * M
dfs(0)
print(answer)

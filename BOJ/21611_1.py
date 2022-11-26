# https://www.acmicpc.net/problem/21611
import sys

d = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
input = sys.stdin.readline


def blank():
    floor = -1
    for idx, r in enumerate(route):
        if board[r[0]][r[1]]:
            tmp = board[r[0]][r[1]]
            board[r[0]][r[1]] = 0
            board[route[floor + 1][0]][route[floor + 1][1]] = tmp
            floor = floor + 1


def destroy():
    res = 0
    cnt = 0
    start = 0
    for idx, r in enumerate(route):
        if board[r[0]][r[1]] == board[route[start][0]][route[start][1]]:
            cnt += 1
        else:
            if cnt > 3:
                color = board[route[start][0]][route[start][1]]
                for rid in range(start, idx):
                    board[route[rid][0]][route[rid][1]] = 0
                res += color * cnt
            if board[r[0]][r[1]] == 0:
                break
            cnt = 1
            start = idx
    return res


def grouping():
    group = []
    cnt = 0
    start = 0
    for idx, r in enumerate(route):
        if board[r[0]][r[1]] == board[route[start][0]][route[start][1]]:
            cnt += 1
        else:
            group.append(cnt)
            group.append(board[route[start][0]][route[start][1]])
            if board[r[0]][r[1]] == 0:
                break
            cnt = 1
            start = idx
    for idx, r in enumerate(route):
        if len(group) <= idx:
            if not board[r[0]][r[1]]:
                break
            board[r[0]][r[1]] = 0
        else:
            board[r[0]][r[1]] = group[idx]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx = N // 2
sy = N // 2
route = []
for k in range(1, N + 1):
    flag = k % 2
    if not flag:
        flag = -1
    for _ in range(k):
        sy -= flag
        route.append((sx, sy))
    if sy == -1:
        route.pop()
        break
    for _ in range(k):
        sx += flag
        route.append((sx, sy))

si = N // 2
sj = N // 2
answer = 0
for _ in range(M):
    dd, ss = map(int, input().split())
    for s in range(1, ss + 1):
        ni = si + d[dd][0] * s
        nj = sj + d[dd][1] * s
        if -1 < ni < N and -1 < nj < N:
            board[ni][nj] = 0

    blank()
    while True:
        a = destroy()
        if not a:
            break
        answer += a
        blank()
    grouping()

print(answer)

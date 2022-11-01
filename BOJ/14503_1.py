# https://www.acmicpc.net/problem/14503
import sys

input = sys.stdin.readline


def move(rr, cc, dd):
    for _ in range(4):
        dd = (dd - 1) % 4
        nr = rr + direction[dd][0]
        nc = cc + direction[dd][1]
        if -1 < nr < N and -1 < nc < M:
            if board[nr][nc] == 0:
                return nr, nc, dd
    return -1, -1, dd


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
while True:
    board[r][c] = -1  # 청소
    answer += 1
    tr, tc, td = move(r, c, d)
    while tr == -1:
        # 후진
        r -= direction[td][0]
        c -= direction[td][1]
        if board[r][c] == 1:
            break
        tr, tc, td = move(r, c, d)
    else:
        r, c, d = tr, tc, td
        continue
    break
print(answer)

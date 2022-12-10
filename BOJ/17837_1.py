# https://www.acmicpc.net/problem/17837
import sys
from collections import defaultdict

input = sys.stdin.readline
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def put(arr, r, c):
    move = r * N + c
    while arr:
        info[move].append(arr.pop())
        loc[info[move][-1][0]] = move
    if len(info[move]) >= 4:
        return False
    return True


def game():
    for i in range(1, K + 1):
        cur = loc[i]  # 말의 위치
        tmp = []  # 움직이는 말
        while info[cur][-1][0] != i:
            tmp.append(info[cur].pop())
        tmp.append(info[cur].pop())
        d = tmp[-1][-1]  # 말의 방향
        x, y = divmod(cur, N)
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if -1 < nx < N and -1 < ny < N and board[nx][ny] != 2:
            if board[nx][ny] == 0: # 흰색
                if not put(tmp, nx, ny):
                    return False
            elif board[nx][ny] == 1:
                if not put(tmp[::-1], nx, ny):
                    return False
        else:
            # 방향을 반대로
            if d == 0 or d == 2:
                d += 1
            elif d == 1 or d == 3:
                d -= 1
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            tmp[-1][-1] = d
            if -1 < nx < N and -1 < ny < N and board[nx][ny] != 2:
                if board[nx][ny] == 0:
                    if not put(tmp, nx, ny):
                        return False
                elif board[nx][ny] == 1:
                    if not put(tmp[::-1], nx, ny):
                        return False
            else:
                while tmp:
                    info[cur].append(tmp.pop())
    return True


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
info = defaultdict(list)
loc = defaultdict(int)
for idx in range(1, K + 1):
    rr, cc, dd = map(int, input().split())
    info[(rr - 1) * N + (cc - 1)].append([idx, dd - 1])
    loc[idx] = (rr - 1) * N + (cc - 1)
answer = 1
while answer < 1001:
    if game():
        answer += 1
    else:
        break
print(answer if answer < 1000 else -1)

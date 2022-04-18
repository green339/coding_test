# https://www.acmicpc.net/problem/20056
import sys
from collections import defaultdict
input = sys.stdin.readline
direction = {6: (0, -1), 7: (-1, -1), 0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1)}

N, M, K = map(int, input().split())
board = defaultdict(list)
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[(r - 1) * N + (c - 1)].append((m, s, d))

for _ in range(K):
    move = defaultdict(list)
    # 1번
    for bk, bv in board.items():
        vx, vy = divmod(bk, N)
        for vm, vs, vd in bv:
            nx = (vx + direction[vd][0] * vs) % N
            ny = (vy + direction[vd][1] * vs) % N
            move[nx * N + ny].append((vm, vs, vd))
    # 2번
    board = defaultdict(list)
    for mk, mv in move.items():
        if len(mv) == 1:
            board[mk].append(*mv)
            continue
        weight = 0
        speed = 0
        odd = 0
        even = 0
        for mm, ms, md in mv:
            weight += mm
            speed += ms
            if md % 2:
                odd += 1
            else:
                even += 1
        weight //= 5
        if weight == 0:
            continue
        speed //= len(mv)
        dd = 0 if not even or not odd else 1
        for idx in range(4):
            board[mk].append((weight, speed, idx * 2 + dd))

answer = 0
for value in board.values():
    for board_value in value:
        answer += board_value[0]
print(answer)

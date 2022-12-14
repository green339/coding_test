# https://www.acmicpc.net/problem/20056
import sys
from collections import defaultdict

input = sys.stdin.readline

d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def move():
    res = defaultdict(list)
    for key, value in board.items():
        if not value:
            continue
        for v in value:
            x, y = divmod(key, N)
            nx = (x + d[v[2]][0] * v[1]) % N
            ny = (y + d[v[2]][1] * v[1]) % N
            res[nx * N + ny].append(v)
    return res


def operation():
    res = defaultdict(list)
    for key, value in board.items():
        if len(value) < 2:
            res[key].append(value[0])
            continue
        cnt = len(value)
        weight = 0
        direction = set()
        speed = 0
        for v in value:
            weight += v[0]
            speed += v[1]
            direction.add(v[2] % 2)
        weight //= 5
        if not weight:
            continue
        speed //= cnt
        for i in range(0, 8, 2):
            res[key].append((weight, speed, i + len(direction) - 1))
    return res


board = defaultdict(list)
N, M, K = map(int, input().split())
for _ in range(M):
    rr, cc, mm, ss, dd = map(int, input().split())
    board[(rr - 1) * N + (cc - 1)].append((mm, ss, dd))

for _ in range(K):
    board = move()
    board = operation()

answer = 0
for value in board.values():
    for v in value:
        answer += v[0]
print(answer)

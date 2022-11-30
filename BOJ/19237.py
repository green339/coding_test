# https://www.acmicpc.net/problem/19237
import sys

input = sys.stdin.readline
direction = {1: (-1, 0), 3: (0, -1), 2: (1, 0), 4: (0, 1)}


def move():
    for fish in range(1, M + 1):
        if fish in die:
            continue
        loc, d = sharks[fish]  # 현재위치, 방향
        # 인접한 위치 탐색
        x, y = divmod(loc, N)
        for idx in order[fish][d]:
            nx = x + direction[idx][0]
            ny = y + direction[idx][1]
            if -1 < nx < N and -1 < ny < N:
                if smell[nx][ny][1] < t:  # 인접한 위치에 빈칸이 있는 경우
                    board[x][y].remove(fish)
                    board[nx][ny].append(fish)
                    sharks[fish] = [nx * N + ny, idx]
                    break
                else:
                    continue
        else:
            for idx in order[fish][d]:
                nx = x + direction[idx][0]
                ny = y + direction[idx][1]
                if -1 < nx < N and -1 < ny < N:
                    if smell[nx][ny][0] == fish:  # 인접한 위치에 자신의 냄새
                        board[x][y].remove(fish)
                        board[nx][ny].append(fish)
                        sharks[fish] = [nx * N + ny, idx]
                        break


def spread():
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                board[i][j].sort()
                while len(board[i][j]) > 1:
                    die.add(board[i][j].pop())
                smell[i][j] = [board[i][j][0], t + k]


N, M, k = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)] # 상어번호, 냄새시간
sharks = dict()
order = dict()
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] != 0:
            board[i][j].append(tmp[j])
            sharks[tmp[j]] = [i * N + j]
            smell[i][j] = [tmp[j], k]
info = list(map(int, input().split()))

for i in range(1, M + 1):
    sharks[i].append(info[i - 1])

for i in range(1, M + 1):
    order[i] = dict()
    for j in range(1, 5):
        order[i][j] = list(map(int, input().split()))
die = set()
t = 0
while len(die) < M - 1 and t < 1001:
    t += 1
    move()
    spread()
print(t if t != 1001 else -1)

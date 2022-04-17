# https://www.acmicpc.net/problem/14503
import sys

input = sys.stdin.readline
d = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

N, M = map(int, input().split())
robot = [list(map(int, input().split()))]
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while robot:
    vx, vy, vd = robot.pop()
    board[vx][vy] = -1
    cnt += 1
    while True:
        for _ in range(4):
            vd = (vd - 1) % 4
            dx, dy = d[vd]
            nx = dx + vx
            ny = dy + vy
            if -1 < nx < N and -1 < ny < M:
                if not board[nx][ny]:
                    robot.append([nx, ny, vd])
                    break
        else:
            if board[vx - d[vd][0]][vy - d[vd][1]] == 1:
                break
            else:
                vx -= d[vd][0]
                vy -= d[vd][1]
                continue
        break
print(cnt)
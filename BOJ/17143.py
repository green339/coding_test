# https://www.acmicpc.net/problem/17143
import sys

input = sys.stdin.readline

direction = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}


def move():
    new_loc = [[[] for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y]:
                s, d, z = board[x][y].pop()
                if d > 2:  # y변경
                    nx = x
                    ny = y + direction[d][1] * s
                    if ny >= C:
                        dist = direction[d][1] * s - (C - 1) + y  # 남은 칸보다 더 움직인 거리
                        a, b = divmod(dist, C - 1)
                        if a % 2:
                            ny = b
                        else:
                            d = 4
                            ny = C - 1 - b
                    elif ny < 0:
                        dist = -direction[d][1] * s - y  # 남은 칸보다 더 움직인 거리
                        a, b = divmod(dist, C - 1)
                        if a % 2:
                            ny = C - 1 - b
                        else:
                            d = 3
                            ny = b
                else:  # x 변경
                    nx = x + direction[d][0] * s
                    ny = y
                    if nx >= R:
                        dist = direction[d][0] * s - (R - 1) + x  # 남은 칸보다 더 움직인 거리
                        a, b = divmod(dist, R - 1)
                        if a % 2:
                            nx = b
                        else:
                            d = 1
                            nx = R - 1 - b
                    elif nx < 0:
                        dist = -direction[d][0] * s - x  # 남은 칸보다 더 움직인 거리
                        a, b = divmod(dist, R - 1)
                        if a % 2:
                            nx = R - 1 - b
                        else:
                            d = 2
                            nx = b
                new_loc[nx][ny].append([s, d, z])
    for x in range(R):
        for y in range(C):
            if new_loc[x][y]:
                board[x][y] = [sorted(new_loc[x][y], key=lambda k: -k[-1])[0]]
            else:
                board[x][y] = []


R, C, M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    xx, yy, ss, dd, zz = map(int, input().split())
    board[xx - 1][yy - 1].append([ss, dd, zz])

answer = 0
for j in range(C):  # 낚시왕의 위치
    # 땅에 가까운 상어를 잡는다
    for i in range(R):
        if board[i][j]:
            answer += board[i][j].pop()[-1]
            break
    # 상어가 이동
    move()
print(answer)

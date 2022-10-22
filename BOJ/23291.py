# https://www.acmicpc.net/problem/23291
import sys

d = [(0, 1), (1, 0)]
input = sys.stdin.readline


def floating():
    height = 1
    width = 0
    start = 0
    for y in range(N):
        height += y % 2
        width += (abs(y % 2 - 1))
        arr = []  # 공중부양
        if height > N - start - width:
            break
        for x in range(height):
            arr.append(board[x][start:start + width])
            board[x][start:start + width] = [0] * width
        start += width
        # arr 반시계방향으로 90도 회전
        arr = list(map(list, zip(*arr)))[::-1]
        for i in range(1, width + 1):
            board[i][start:start + height] = arr[i - 1]
    return start, height, width


def control(s, h):
    res = [[0] * N for _ in range(M)]
    for i in range(0, h):
        for j in range(s, N):
            if board[i][j]:
                for di, dj in d:
                    ni = di + i
                    nj = dj + j
                    if -1 < ni < M and -1 < nj < N:
                        if board[ni][nj]:
                            diff = abs(board[i][j] - board[ni][nj]) // 5
                            if board[i][j] > board[ni][nj]:
                                res[i][j] -= diff
                                res[ni][nj] += diff
                            elif board[i][j] < board[ni][nj]:
                                res[i][j] += diff
                                res[ni][nj] -= diff
    row = []
    for j in range(s, N):
        for i in range(0, h):
            if board[i][j]:
                board[i][j] += res[i][j]
                row.append(board[i][j])
                board[i][j] = 0
    return row


def control_2(arr, part):
    res = [[0] * part for _ in range(4)]
    for i in range(4):
        for j in range(part):
            for di, dj in d:
                ni = di + i
                nj = dj + j
                if -1 < ni < 4 and -1 < nj < part:
                    diff = abs(arr[i][j] - arr[ni][nj]) // 5
                    if arr[i][j] > arr[ni][nj]:
                        res[i][j] -= diff
                        res[ni][nj] += diff
                    elif arr[i][j] < arr[ni][nj]:
                        res[i][j] += diff
                        res[ni][nj] -= diff
    row = []
    for j in range(part):
        for i in range(3, -1, -1):
            arr[i][j] += res[i][j]
            row.append(arr[i][j])
    return row


N, K = map(int, input().split())
M = N // 2
board = [[0] * N for _ in range(M)]
tmp = list(map(int, input().split()))
# 처음에 주어진 어항이 조건만족
if max(tmp) - min(tmp) <= K:
    print(0)
    exit()
for j in range(N):
    board[0][j] = tmp[j]
answer = 1
while True:
    # 가장 작은 어항에 물고기 한마리씩
    min_fish = min(board[0])
    for y in range(N):
        if board[0][y] == min_fish:
            board[0][y] += 1
    # 공중부양
    ss, hh, ww = floating()
    p = N // 4
    # 물고기수 조절
    line = control(ss, hh)
    #  공중부양2
    line = [line[2 * p:3 * p][::-1], line[p:2 * p], line[:p][::-1], line[3 * p:4 * p]]
    line_2 = control_2(line, p)
    board[0] = line_2
    # 차이가 K이하면 멈춤
    if max(board[0]) - min(board[0]) <= K:
        break
    answer += 1
print(answer)

# # https://www.acmicpc.net/problem/19236
import sys
from copy import deepcopy

input = sys.stdin.readline
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def dfs(dfs_board, dfs_fish, cur, sx, sy, sd):
    global answer

    def move():
        for num in range(1,17):
            fish_x, fish_y, fish_dd = fish[num] # 물고기 정보
            if num != board[fish_x][fish_y]:  # 잡아먹힌 경우
                continue
            for di in range(8):
                fish_d = (fish_dd + di) % 8
                nx = fish_x + direction[fish_d][0]
                ny = fish_y + direction[fish_d][1]
                if -1 < nx < 4 and -1 < ny < 4:
                    if board[nx][ny] == -1: # 상어가 있는 경우
                        continue
                    if not board[nx][ny]: # 물고기가 없는 경우
                        board[fish_x][fish_y] = 0
                    else: # 물고기가 있는 경우
                        exist_num = board[nx][ny]
                        board[fish_x][fish_y] = exist_num
                        fish[exist_num][0] = fish_x
                        fish[exist_num][1] = fish_y
                    board[nx][ny] = num
                    fish[num] = [nx, ny, fish_d]
                    break
                else: # 경계를 넘어가는 경우
                    continue

    answer = max(answer, cur)
    board = deepcopy(dfs_board)
    fish = deepcopy(dfs_fish)
    # 상어이동
    move()
    # 먹을 수 있는 곳들 탐색
    board[sx][sy] = 0
    start = 0
    while -1 < sx < 4 and -1 < sy < 4:
        if board[sx][sy] > 0:
            tmp = board[sx][sy]
            board[sx][sy] = -1
            dfs(board, fish, cur + tmp, sx, sy, fish[tmp][-1])
            board[sx][sy] = tmp
        start += 1
        sx += direction[sd][0]
        sy += direction[sd][1]


answer = 0
fish_info = dict()  # 위치x,y,방향
arr = []  # 물고기 번호
for i in range(4):
    tmp = list(map(int, input().split()))
    row = []
    for j in range(0, 8, 2):
        row.append(tmp[j])
        fish_info[tmp[j]] = [i, j // 2, tmp[j + 1] - 1]
    arr.append(row)
# 초기상태
answer = arr[0][0]
arr[0][0] = -1  # 상어의 위치
dfs(arr, fish_info, answer, 0, 0, fish_info[answer][-1])
print(answer)

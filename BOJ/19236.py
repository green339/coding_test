# https://www.acmicpc.net/problem/19236
from copy import deepcopy


def move(board, fish):
    for idx in range(1, 17):  # 작은 수 부터 차례로 이동
        if visited[idx]:
            continue
        x, y, d = fish[idx]
        for _ in range(8):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            if -1 < nx < 4 and -1 < ny < 4:
                if board[nx][ny] != -1:  # 바꿀 수 잇는 경우
                    break
            d = (d + 1) % 8
        else:
            continue
        # 그칸에 있는 거랑 서로 바꿈
        if board[nx][ny]:
            fish[board[nx][ny]][0] = x
            fish[board[nx][ny]][1] = y
        fish[board[x][y]] = [nx, ny, d]
        tmp = board[x][y]
        board[x][y] = board[nx][ny]
        board[nx][ny] = tmp
    return board, fish


def solution(board, fish, sx, sy, sd, depth):
    global answer
    board_tmp, fish_tmp = move(board, fish)
    flag = 0
    for l in range(1, 4):
        nsx = sx + direction[sd][0] * l
        nsy = sy + direction[sd][1] * l
        if -1 < nsx < 4 and -1 < nsy < 4:
            if board_tmp[nsx][nsy] > 0:
                flag = 1  # 한번이라도 이동함
                ate = board_tmp[nsx][nsy]
                nsd = fish_tmp[ate][-1]
                visited[ate] = 1
                board_tmp[nsx][nsy] = -1
                board_tmp[sx][sy] = 0

                copy_board = deepcopy(board_tmp)
                copy_fish = deepcopy(fish_tmp)
                solution(copy_board, copy_fish, nsx, nsy, nsd, depth + 1)

                board_tmp[nsx][nsy] = ate
                visited[ate] = 0
                board_tmp[sx][sy] = -1
        else:
            break
    if not flag:  # 이동할 곳이 없는 경우
        number = 0
        for n in range(1, 17):
            if visited[n]:
                number += n
        answer = max(answer, number)
        return


direction = {0: (-1, 0), 1: (-1, -1), 2: (0, -1), 3: (1, -1), 4: (1, 0), 5: (1, 1), 6: (0, 1), 7: (-1, 1)}
temp = [list(map(int, input().split())) for _ in range(4)]
fish_info = dict()  # 몇 번 물고기가 어디에 있는지
arr = [[0] * 4 for _ in range(4)]  # 상어랑 물고기 위치 한번에 보기
for i in range(4):
    for j in range(4):
        a = temp[i][2 * j]
        b = temp[i][2 * j + 1] - 1
        fish_info[a] = [i, j, b]
        arr[i][j] = a
visited = [0] * 17
visited[arr[0][0]] = 1
ssx, ssy, ssd = fish_info[arr[0][0]]
arr[0][0] = -1
answer = 0
solution(arr, fish_info, ssx, ssy, ssd, 0)
print(answer)

# https://www.acmicpc.net/problem/23290
import copy


def dfs(depth, arr, temp):
    global cnt, route
    if depth == 3:
        if temp > cnt:
            route = copy.deepcopy(arr)
            cnt = temp
        return
    # 상어 이동
    if arr:
        ssx = arr[-1][0]
        ssy = arr[-1][1]
    else:
        ssx=sx
        ssy=sy
    for sd in [2, 0, 6, 4]:
        nsx = ssx + direction[sd][0]
        nsy = ssy + direction[sd][1]
        if -1 < nsx < 4 and -1 < nsy < 4:
            if (nsx, nsy) not in arr:
                arr.append((nsx, nsy))
                dfs(depth + 1, arr, temp + len(board[nsx][nsy]))
                arr.pop()
            else:
                arr.append((nsx,nsy))
                dfs(depth+1,arr,temp)
                arr.pop()


def move():
    global board
    temp = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            for d in board[x][y]:
                for i in range(8):
                    nd = (d - i) % 8
                    nx = x + direction[nd][0]
                    ny = y + direction[nd][1]
                    if nx == sx and ny == sy:  # 상어가 있는 경우
                        continue
                    if -1 < nx < 4 and -1 < ny < 4:
                        if t - smell[nx][ny] < 3:  # 냄새가 있는 경우
                            continue
                        temp[nx][ny].append(nd)
                        break
                else:
                    temp[x][y].append(d)
    board = copy.deepcopy(temp)


direction = {0: (0, -1), 1: (-1, -1), 2: (-1, 0), 3: (-1, 1), 4: (0, 1), 5: (1, 1), 6: (1, 0), 7: (1, -1)}
board = [[[] for _ in range(4)] for _ in range(4)]
smell = [[-3] * 4 for _ in range(4)]  # 물고기 냄새 저장 (삭제할 물고기들 저장)
M, S = map(int, input().split())
for _ in range(M):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1].append(d - 1)
sx, sy = map(int, input().split())
sx -= 1
sy -= 1
cnt = -1
route = []

for t in range(S):
    # 복제마법
    temp_board = copy.deepcopy(board)
    # 이동
    move()
    # 상어이동
    dfs(0, [], 0)
    for sx,sy in route:
        if board[sx][sy]:
            board[sx][sy] = []
            smell[sx][sy] = t
    route = []
    cnt = -1
    # 복제
    for x in range(4):
        for y in range(4):
            for td in temp_board[x][y]:
                board[x][y].append(td)
answer = 0
for x in range(4):
    for y in range(4):
        if board[x][y]:
            answer += len(board[x][y])
print(answer)

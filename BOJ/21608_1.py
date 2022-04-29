# https://www.acmicpc.net/problem/21608
# 2:40


direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())
student = dict()
board = [[0] * N for _ in range(N)]
for _ in range(N ** 2):
    a, b, c, d, e = map(int, input().split())
    student[a] = {b, c, d, e}
score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
answer = 0
for k, v in student.items():
    like = 0
    space = 0
    lx, ly = (0, 0)
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                continue
            space_cnt = 0
            like_cnt = 0
            for di, dj in direction:
                ni = di + i
                nj = dj + j
                if -1 < ni < N and -1 < nj < N:
                    if board[ni][nj]:
                        if board[ni][nj] in v:
                            like_cnt += 1
                    else:
                        space_cnt += 1
            if like_cnt > like or (like_cnt == like and space_cnt > space):
                like = like_cnt
                lx, ly = i, j
                space = space_cnt
            elif space_cnt == 0 and like_cnt == 0 and board[lx][ly]: # 0,0에서 계속 멈춰있는 경우
                lx, ly = i, j
    board[lx][ly] = k
cnt = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for di, dj in direction:
            ni = di + i
            nj = dj + j
            if -1 < ni < N and -1 < nj < N:
                if board[ni][nj] in student[board[i][j]]:
                    cnt += 1
        answer += score[cnt]

print(answer)

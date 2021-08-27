import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = 0
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(N):
    for j in range(N):
        flag = 1
        for dx, dy in d:
            nx = dx + i
            ny = dy + j
            if -1 < nx < N and -1 < ny < N:
                if board[i][j] <= board[nx][ny]:
                    flag = 0
                    break
        if flag:
            count += 1
print(count)

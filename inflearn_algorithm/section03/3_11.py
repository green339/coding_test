import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(7)]

count = 0
for s in range(3):
    for j in range(7):
        e = s + 4
        # 세로
        flag1 = 1
        for n in range(2):
            if board[s + n][j] != board[e - n][j]:
                flag1 = 0
                break
        # 가로
        flag2 = 1
        for n in range(2):
            # print(board[j][s + n] , board[j][e - n])
            if board[j][s + n] != board[j][e - n]:
                flag2 = 0
                break
        count += (flag1 + flag2)
print(count)

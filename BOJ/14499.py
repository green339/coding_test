# https://www.acmicpc.net/problem/14499
import sys
input = sys.stdin.readline
d = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}

if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    command = list(map(int, input().split()))
    dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    status = (1, 3, 5)

    for c in command:
        nx = x + d[c][0]
        ny = y + d[c][1]
        if not (-1 < nx < N and -1 < ny < M):
            continue
        if c == 1:
            status = (abs(7 - status[1]), status[0], status[2])
        elif c == 2:
            status = (status[1], abs(status[0] - 7), status[2])
        elif c == 3:
            status = (status[2], status[1], abs(7 - status[0]))
        elif c == 4:
            status = (abs(7 - status[2]), status[1], status[0])
        x = nx
        y = ny
        if board[x][y]:
            dice[abs(7 - status[0])] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[abs(7 - status[0])]
        print(dice[status[0]])

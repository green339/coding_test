# https://www.acmicpc.net/problem/2580
import sys

input = sys.stdin.readline


def check(x, y):
    for k in range(9):
        if k != x and board[k][y] == board[x][y]:
            return False
        if k != y and board[x][k] == board[x][y]:
            return False
    mx = 3 * (x // 3)
    my = 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            nx = mx + i
            ny = my + j
            if nx != x and ny != y and board[nx][ny] == board[x][y]:
                return False
    return True


def backtracking(cur):
    if cur == 81:
        for b in board:
            print(*b)
        exit(0)
    x = cur // 9
    y = cur % 9
    if board[x][y]:
        backtracking(cur + 1)
    else:
        for n in numbers:
            board[x][y] = n
            if check(x, y):
                backtracking(cur + 1)
            board[x][y] = 0


board = [list(map(int, input().split())) for _ in range(9)]
answer = [[0] * 9 for _ in range(9)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
backtracking(0)

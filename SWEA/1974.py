import sys

input = sys.stdin.readline


def check():
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            if row[board[i][j]] > 0 or col[board[j][i]] == 1:
                return 0
            col[board[j][i]] = 1
            row[board[i][j]] = 1
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [0] * 10
            for r in range(3):
                for c in range(3):
                    if square[board[i + r][j + c]] == 1:
                        return 0
                    square[board[i + r][j + c]] = 1
    return 1


tc = int(input())
for test_case in range(1, tc + 1):
    answer = 1
    board = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test_case} {check()}')
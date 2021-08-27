import sys


def check(board):
    for x in range(9):
        for y in range(9):
            for i in range(9):
                if i != y and board[x][y] == board[x][i]:
                    return "NO"
                if i != x and board[x][y] == board[i][y]:
                    return "NO"
            br = (x // 3) * 3
            bc = (y // 3) * 3
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    if board[x][y] == board[r][c] and x != r and x != c:
                        return "NO"
    return "YES"


sdoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
print(check(sdoku))

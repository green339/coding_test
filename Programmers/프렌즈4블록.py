# https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in zip(*board)]
    while True:
        erase = [[0] * m for _ in range(n)]
        flag = 0
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] and len({board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1]}) == 1:
                    flag = 1
                    erase[i][j] = 1
                    erase[i + 1][j] = 1
                    erase[i][j + 1] = 1
                    erase[i + 1][j + 1] = 1
        if flag:
            for r in range(n):
                for c in range(m):
                    if erase[r][c]:
                        board[r][c] = 0
                        answer += 1
                while 0 in board[r]:
                    board[r].remove(0)
                    board[r].insert(0, "")
        else:
            break
    return answer

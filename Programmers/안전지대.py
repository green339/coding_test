# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    n = len(board)
    mine = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                mine.append([i, j])
    for i, j in mine:
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            ni = di + i
            nj = dj + j
            if -1 < ni < n and -1 < nj < n:
                board[ni][nj] = 1
    answer = n * n - sum(map(sum, board))
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    board = [[0] * i for i in range(1, n + 1)]
    cur = 1
    y = 0
    x = -1
    while n > 0:
        for _ in range(n):
            x += 1
            board[x][y] = cur
            cur += 1
        for _ in range(n - 1):
            y += 1
            board[x][y] = cur
            cur += 1
        for _ in range(n - 2):
            x -= 1
            y -= 1
            board[x][y] = cur
            cur += 1
        n -= 3
    for b in board:
        answer.extend(b)
    return answer

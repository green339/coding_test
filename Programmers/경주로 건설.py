# https://programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque


def solution(board):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    n = len(board)
    visit = [[[10e9, 10e9, 10e9, 10e9] for _ in range(n)] for _ in range(n)]
    dq = deque()

    dq.append((0, 0, 0, 0))
    dq.append((0, 0, 0, 1))

    while (dq):
        nx, ny, c, state = dq.popleft()
        for i in range(4):
            temp = c + 100
            vx = nx + dx[i]
            vy = ny + dy[i]
            if -1 < vx < n and -1 < vy < n and board[vx][vy] == 0:
                if state != i:
                    temp += 500
                if visit[vx][vy][i] > temp:
                    visit[vx][vy][i] = temp
                    dq.append((vx, vy, temp, i))

    answer = min(visit[n - 1][n - 1])
    return answer

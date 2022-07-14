# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque


def solution(board):
    n = len(board)
    q = deque()
    q.append((0, 1, 0))  # 기준을 가로면 오른쪽, 세로면 아래
    d = [-2, 1]
    dr = [1, -1]
    visited = [[[10e9, 10e9] for _ in range(n)] for _ in range(n)]  # 0이면 가로, 1이면 세로
    visited[0][1][0] = 0
    while q:
        x, y, flag = q.popleft()
        cost = visited[x][y][flag]
        if flag:  # 세로로
            # 위 아래로 움직이는 경우
            for dx in d:
                nx = x + dx
                mx = max(x - 1, nx)
                if -1 < nx < n and not board[nx][y]:
                    if visited[mx][y][flag] > cost + 1:
                        visited[mx][y][flag] = cost + 1
                        q.append((mx, y, flag))
            for dy in dr:
                ny = y + dy
                if -1 < ny < n and not board[x - 1][ny] and not board[x][ny]:
                    # 회전하는 경우
                    my = max(y, ny)
                    if visited[x][my][flag - 1] > cost + 1:
                        visited[x][my][flag - 1] = cost + 1
                        q.append((x, my, flag - 1))
                    if visited[x - 1][my][flag - 1] > cost + 1:
                        visited[x - 1][my][flag - 1] = cost + 1
                        q.append((x - 1, my, flag - 1))
                    # 왼 오로 움직이는 경우
                    if visited[x][ny][flag] > cost + 1:
                        visited[x][ny][flag] = cost + 1
                        q.append((x, ny, flag))
        else:  # 가로로
            # 왼 오로 움직이는 경우
            for dy in d:
                ny = y + dy
                my = max(y - 1, ny)
                if -1 < ny < n and not board[x][ny]:
                    if visited[x][my][flag] > cost + 1:
                        visited[x][my][flag] = cost + 1
                        q.append((x, my, flag))
            for dx in dr:
                nx = x + dx
                if -1 < nx < n and not board[nx][y - 1] and not board[nx][y]:
                    # 회전하는 경우
                    mx = max(x, nx)
                    if visited[mx][y][flag + 1] > cost + 1:
                        visited[mx][y][flag + 1] = cost + 1
                        q.append((mx, y, flag + 1))
                    if visited[mx][y - 1][flag + 1] > cost + 1:
                        visited[mx][y - 1][flag + 1] = cost + 1
                        q.append((mx, y - 1, flag + 1))
                    # 위 아래로 움직이는 경우
                    if visited[nx][y][flag] > cost + 1:
                        visited[nx][y][flag] = cost + 1
                        q.append((nx, y, flag))
    return min(visited[-1][-1])

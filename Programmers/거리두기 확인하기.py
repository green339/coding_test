# https://programmers.co.kr/learn/courses/30/lessons/81302
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def check(board, x, y):
    q = deque()
    visited = set()
    q.append((0, x, y))
    visited.add((x, y))
    while q:
        ml, sx, sy = q.popleft()
        if ml == 2:
            continue
        for dx, dy in direction:
            nx = dx + sx
            ny = dy + sy
            if -1 < nx < 5 and -1 < ny < 5 and (nx, ny) not in visited:
                if board[nx][ny] == 'O':
                    q.append((ml + 1, nx, ny))
                    visited.add((nx, ny))
                elif board[nx][ny] == 'P':
                    return 0
    return 1


def solution(places):
    answer = []
    for p in places:
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    if not check(p, i, j):
                        answer.append(0)
                        break
            else:
                continue
            break
        else:
            answer.append(1)
    return answer

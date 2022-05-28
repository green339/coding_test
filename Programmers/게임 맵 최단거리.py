# https://programmers.co.kr/learn/courses/30/lessons/1844
import heapq


def solution(maps):
    answer = 0
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    q = [(0, 0, 0)]
    n = len(maps)
    m = len(maps[0])
    while q:
        c, x, y = heapq.heappop(q)
        if x == n - 1 and y == m - 1:
            return c + 1
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if -1 < nx < n and -1 < ny < m:
                if maps[nx][ny]:
                    maps[nx][ny] = 0
                    heapq.heappush(q, (c + 1, nx, ny))
    return -1


from collections import deque

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def solution_v2(maps):
    answer = 0
    n = len(maps) - 1
    m = len(maps[0]) - 1
    q = deque()
    q.append((0, 0))
    maps[0][0] = 2
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if -1 < nx <= n and -1 < ny <= m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
    return maps[n][m] - 1 if maps[n][m] != 1 else -1

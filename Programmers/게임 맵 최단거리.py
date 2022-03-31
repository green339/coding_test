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

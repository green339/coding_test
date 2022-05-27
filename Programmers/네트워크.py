# https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque, defaultdict


def solution(n, computers):
    answer = 0
    visited = [0] * n
    q = deque()
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        q.append(i)
        while q:
            x = q.popleft()
            for dx in range(n):
                if computers[x][dx] and not visited[dx]:
                    q.append(dx)
                    visited[dx] = 1
        answer += 1
    return answer


# 220527
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        x = q.popleft()
        for nx in board[x]:
            if not visited[nx]:
                visited[nx] = 1
                q.append(nx)
    return 1


def solution_v2(n, computers):
    answer = 0
    global visited
    visited = [0] * n
    global board
    board = defaultdict(set)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                board[i].add(j)
                board[j].add(i)
    for i in range(n):
        if not visited[i]:
            answer += bfs(i)
    return answer

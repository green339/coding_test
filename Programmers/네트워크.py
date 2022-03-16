# https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque


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

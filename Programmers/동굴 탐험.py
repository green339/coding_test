# https://programmers.co.kr/learn/courses/30/lessons/67260
from collections import defaultdict, deque


def solution(n, path, order):
    answer = True
    warn = defaultdict(int)
    for f, s in order:
        warn[s] = f
    board = defaultdict(list)
    for i, j in path:
        board[i].append(j)
        board[j].append(i)
    visited = [0] * n
    q = deque()
    q.append(0)
    visited[0] = 1
    waiting = defaultdict(int)
    while q:
        n = q.popleft()
        if n in warn.keys() and visited[warn[n]] == 0:
            waiting[warn[n]] = n
            continue
        for v in board[n]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1
                if v in waiting.keys():
                    q.append(waiting[v])
                    del waiting[v]

    if min(visited) == 0:
        answer = False
    return answer

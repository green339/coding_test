# https://school.programmers.co.kr/learn/courses/30/lessons/76503#qna
from collections import deque, defaultdict


def solution(a, edges):
    if sum(a):
        return -1
    n = len(a)
    answer = 0
    board = defaultdict(set)
    indegree = [0] * n
    for u, v in edges:
        board[u].add(v)
        board[v].add(u)
        indegree[u] += 1
        indegree[v] += 1
    q = deque()
    visited = [0] * n
    for i in range(n):
        if len(board[i]) == 1:
            q.append(i)
    while q:
        pre_node = q.popleft()
        visited[pre_node] = 1
        for post_node in board[pre_node]:
            if not visited[post_node]:
                answer += abs(a[pre_node])
                a[post_node] += a[pre_node]
                indegree[post_node] -= 1
                if indegree[post_node] == 1:
                    q.append(post_node)
    return answer

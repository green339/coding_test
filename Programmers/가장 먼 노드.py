# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque, defaultdict


def solution(n, edge):
    distance = [10e9] * (n + 1)
    distance[0] = 0
    distance[1] = 0
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque()
    q.append(1)
    while q:
        nx = q.popleft()
        for g in graph[nx]:
            if distance[nx] + 1 < distance[g]:
                distance[g] = distance[nx] + 1
                q.append(g)

    distance.sort(reverse=True)
    answer = distance.count(distance[0])

    return answer


def solution_v2(n, edge):
    visited = [0] * (n + 1)
    board = defaultdict(set)
    for n1, n2 in edge:
        board[n1].add(n2)
        board[n2].add(n1)
    visited[1] = 1
    answer = 0
    dist = 0
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        if visited[x] == dist:
            answer += 1
        elif visited[x] > dist:
            dist = visited[x]
            answer = 1
        for b in board[x]:
            if not visited[b]:
                q.append(b)
                visited[b] = visited[x] + 1
    return answer

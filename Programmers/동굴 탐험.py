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


def solution_v2(n, path, order):
    # 진입차수 (0 빼고는 적어도 1)
    indegree = [1] * n
    indegree[0] = 0
    board = defaultdict(list)
    for a, b in path:
        board[a].append(b)
        board[b].append(a)
    # 단방향 그래프 만들기
    graph = defaultdict(list)
    visited = [0] * n
    q = deque()
    q.append(0)
    visited[0] = 1
    while q:
        x = q.popleft()
        for nx in board[x]:
            if not visited[nx]:
                visited[nx] = 1
                q.append(nx)
                graph[x].append(nx)
    for a, b in order:
        graph[a].append(b)
        indegree[b] += 1
    # 위상정렬
    q = deque()
    q.append(0)
    cnt = 0
    while q:
        cnt += 1
        pre_node = q.popleft()
        for post_node in graph[pre_node]:
            indegree[post_node] -= 1
            if not indegree[post_node]:
                q.append(post_node)
    return cnt == n

# https://programmers.co.kr/learn/courses/30/lessons/86971
from collections import defaultdict, deque


def bfs(k, e):
    exclude = {(k, e), (e, k)}
    q = deque()
    q.append(k)
    towers = [0] + [-1] * (len(board.keys()))
    towers[k] = 1
    while q:
        x = q.popleft()
        for nx in board[x]:
            if (x, nx) in exclude:
                continue
            if towers[nx] == -1:
                towers[nx] = 1
                q.append(nx)
    return abs(sum(towers))


def solution(n, wires):
    answer = 100
    global board
    board = defaultdict(list)
    for v1, v2 in wires:
        board[v1].append(v2)
        board[v2].append(v1)
    for k, v in sorted(board.items()):
        for e in v:
            if k > e:
                continue
            answer = min(bfs(k, e), answer)
    return answer

# union-find로 풀어보기

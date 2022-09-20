# https://programmers.co.kr/learn/courses/30/lessons/72413
def solution(n, s, a, b, fares):
    INF = 10e9
    board = [[INF] * (n + 1) for _ in range(n + 1)]
    for k in range(n + 1):
        board[k][k] = 0
    for i, j, c in fares:
        board[i][j] = c
        board[j][i] = c
    for w in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                if board[x][y] > board[x][w] + board[w][y]:
                    board[x][y] = board[x][w] + board[w][y]

    answer = board[s][a] + board[s][b]
    for i in range(n + 1):
        answer = min(answer, board[s][i] + board[i][a] + board[i][b])

    return answer


from collections import defaultdict
import heapq


def solution_v2(n, s, a, b, fares):
    def distance(sx):
        dist = [10e9] * (n + 1)
        q = [(0, sx)]
        dist[sx] = 0
        while q:
            cur, x = heapq.heappop(q)
            if dist[x] < cur:
                continue
            for nx, cost in board[x]:
                tmp = cost + cur
                if tmp < dist[nx]:
                    dist[nx] = tmp
                    heapq.heappush(q, (tmp, nx))
        return dist

    board = defaultdict(list)
    for c, d, f in fares:
        board[c].append((d, f))
        board[d].append((c, f))
    distances = [0] * (n + 1)
    for k in [s, a, b]:
        tmp = distance(k)
        for idx in range(n + 1):
            distances[idx] += tmp[idx]
    return min(distances)

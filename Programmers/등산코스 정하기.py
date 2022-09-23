# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict
import heapq

inf = 10000001


def solution(n, paths, gates, summits):
    def d():
        distance = [inf] * (n + 1)
        q = []
        for start in gates:
            heapq.heappush(q, (0, start))
            distance[start] = 0
        while q:
            cur, x = heapq.heappop(q)
            if x in summitset:
                continue
            if distance[x] < cur:
                continue
            for nx, cost in board[x]:
                tmp = max(cost, cur)
                if distance[nx] > tmp:
                    distance[nx] = tmp
                    heapq.heappush(q, (tmp, nx))
        return distance

    summits.sort()  # 정렬!
    summitset = set(summits)
    board = defaultdict(list)
    for i, j, w in paths:
        board[i].append((j, w))
        board[j].append((i, w))
    dist = d()
    answer = [0, inf]
    for s in summits:
        if answer[1] > dist[s]:
            answer[0] = s
            answer[1] = dist[s]
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq
from collections import defaultdict

inf = 10e9


def solution(N, road, K):
    answer = 0
    board = defaultdict(list)
    for a, b, c in road:
        board[a].append((b, c))
        board[b].append((a, c))

    # 다익스트라 1번부터
    distance = [inf] * (N + 1)
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, current = heapq.heappop(q)
        if distance[current] < dist:
            continue
        for idx, cost in board[current]:
            temp = dist + cost
            if temp < distance[idx]:
                distance[idx] = temp
                heapq.heappush(q, (temp, idx))

    for d in distance:
        if d <= K:
            answer += 1
    return answer

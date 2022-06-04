# https://programmers.co.kr/learn/courses/30/lessons/42628

from collections import deque
import heapq


def adding(q, e):
    idx = len(q)
    l, r = 0, len(q) - 1
    while l <= r:
        mid = (l + r) // 2
        if e <= q[mid]:
            idx = mid
            l = mid + 1
        else:
            r = mid - 1
    return idx


def solution(operations):
    q = deque()
    for op in operations:
        c, n = op.split(" ")
        n = int(n)
        if c == "I":
            if q:
                q.insert(adding(q, n), n)
            else:
                q.append(n)
        else:
            if q:
                if n == -1:
                    q.popleft()
                else:
                    q.pop()
    return [q[-1], q[0]] if q else [0, 0]


def solution_v2(operations):
    min_hq = []
    max_hq = []
    for o in operations:
        o = o.split(" ")
        if o[0] == 'I':
            heapq.heappush(min_hq, int(o[1]))
            heapq.heappush(max_hq, -int(o[1]))
        else:
            if min_hq:
                if int(o[1]) > 0:
                    min_hq.remove(-heapq.heappop(max_hq))
                else:
                    max_hq.remove(-heapq.heappop(min_hq))
    return [-max_hq[0], min_hq[0]] if min_hq else [0, 0]

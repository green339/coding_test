# https://programmers.co.kr/learn/courses/30/lessons/42628

from collections import deque


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
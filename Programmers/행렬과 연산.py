# https://school.programmers.co.kr/learn/courses/30/lessons/118670
from collections import deque


def solution(rc, operations):
    rows = deque(deque(r[1:-1]) for r in rc)
    tmp = deque(map(deque, zip(*rc)))
    cols = deque([tmp[0], tmp[-1]])
    for op in operations:
        if op == "ShiftRow":
            rows.rotate(1)
            cols[0].rotate(1)
            cols[1].rotate(1)
        else:
            rows[-1].append(cols[-1].pop())
            cols[0].append(rows[-1].popleft())
            rows[0].appendleft(cols[0].popleft())
            cols[-1].appendleft(rows[0].pop())
    rows = deque(map(deque, zip(*rows)))
    rows.appendleft(cols[0])
    rows.append(cols[1])
    return list(zip(*rows))

# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    q = deque()
    for n, p in enumerate(priorities):
        q.append((n, p))
    priorities.sort()
    cnt = 0
    temp_max = priorities.pop()
    while True:
        nx, px = q.popleft()
        if px == temp_max:
            cnt += 1
            if nx == location:
                return cnt
            temp_max = priorities.pop()
        else:
            q.append((nx, px))

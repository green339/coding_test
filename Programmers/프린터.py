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


def solution_v2(priorities, location):
    answer = 0
    cur = 0
    end = len(priorities)
    while sum(priorities) > 0:
        if not priorities[cur]:
            cur = (cur + 1) % end
            continue
        for x in range(cur + 1, cur + end):
            if priorities[cur] < priorities[x % end]:
                break
        else:
            priorities[cur] = 0
            answer += 1
            if cur == location:
                return answer
        cur = (cur + 1) % end
    return answer

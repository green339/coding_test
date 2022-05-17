# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5
    answer = 0
    cache = deque()
    for c in cities:
        c = c.lower()
        if c in cache:
            answer += 1
            cache.remove(c)
        else:
            answer += 5
            if cache and len(cache) == cacheSize:
                cache.popleft()
        cache.append(c)
    return answer


def solution_v2(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    answer = 0
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            answer += 5
            cache.append(c)
    return answer

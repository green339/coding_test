# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for c in course:
        cnt = defaultdict(int)
        for o in orders:
            for i in combinations(sorted(o), c):
                cnt[''.join(i)] += 1
        if cnt:
            temp = max(cnt.values())
        else:
            continue
        if temp < 2:
            continue
        for k, v in cnt.items():
            if v == temp:
                answer.append(k)

    answer.sort()
    return answer

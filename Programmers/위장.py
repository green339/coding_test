# https://programmers.co.kr/learn/courses/30/lessons/42578
from collections import defaultdict


def solution(clothes):
    answer = 1
    spy = defaultdict(int)
    for c, k in clothes:
        spy[k] += 1

    for cs in spy.values():
        answer *= (cs + 1)

    return answer - 1

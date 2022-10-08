# https://school.programmers.co.kr/learn/courses/30/lessons/120812
from collections import Counter


def solution(array):
    if len(array) == 1: return array[0]
    cnt = Counter(array).most_common(2)
    return cnt[0][0] if cnt[0][1] != cnt[1][1] else -1

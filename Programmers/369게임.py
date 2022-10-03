# https://school.programmers.co.kr/learn/courses/30/lessons/120891
from collections import Counter


def solution(order):
    cnt = Counter(str(order))
    return cnt["3"] + cnt["6"] + cnt["9"]

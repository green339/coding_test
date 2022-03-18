# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    answer = []
    l = len(relation[0])
    s = len(relation)
    size = [i for i in range(l)]
    attribute = list(zip(*relation))
    for r in range(1, l + 1):
        for k in combinations(size, r):
            # minimality
            for x in range(1, len(k) + 1):
                if set(answer) & set(combinations(k, x)):
                    break
            else:
                temp = [attribute[idx] for idx in k]
                # uniqueness
                if len(set(zip(*temp))) == s:
                    answer.append(k)
    return len(answer)

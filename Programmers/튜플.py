from collections import defaultdict


def solution(s):
    temp = [a.split(',') for a in s[2:-2].split("},{")]
    elements = defaultdict(int)
    for t in temp:
        for x in t:
            elements[x] += 1
    return list(map(int, sorted(elements, key=lambda k: elements[k], reverse=True)))

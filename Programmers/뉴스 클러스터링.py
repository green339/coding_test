# https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import defaultdict


def make_elemet(s):
    agg = set()
    count = defaultdict(int)
    for idx in range(len(s) - 1):
        if not (s[idx].isalpha() and s[idx + 1].isalpha()):
            continue
        pair = s[idx].lower() + s[idx + 1].lower()
        count[pair] += 1
        agg.add(pair + str(count[pair]))
    return agg


def solution(str1, str2):
    A = make_elemet(str1)
    B = make_elemet(str2)
    return int(len(A & B) / len(A | B) * 65536) if A or B else 65536

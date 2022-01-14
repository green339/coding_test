# https://programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict


def solution(id_list, report, k):
    warn = defaultdict(set)
    for r in set(report):
        r = r.split()
        warn[r[1]].add(r[0])
    mail = defaultdict(int)
    for key, value in warn.items():
        if len(value) >= k: # 신고당한 횟수
            for usr in value:
                mail[usr] += 1
    answer = [mail[i] for i in id_list]
    return answer

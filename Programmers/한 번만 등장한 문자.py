# https://school.programmers.co.kr/learn/courses/30/lessons/120896
from collections import Counter


def solution(s):
    answer = ''
    for k, v in sorted(Counter(s).items(), key=lambda x: (x[1], x[0])):
        if v > 1:
            break
        answer += k
    return answer


def solution_v2(s):
    return "".join(sorted([ss for ss in s if s.count(ss) == 1]))

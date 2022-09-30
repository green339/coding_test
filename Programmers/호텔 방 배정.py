# https://school.programmers.co.kr/learn/courses/30/lessons/64063
from collections import defaultdict


def solution(k, room_number):
    answer = []
    lnk = defaultdict(int)
    for rm in room_number:
        tmp = []
        while lnk[rm]:
            tmp.append(rm)
            rm = lnk[rm]
        answer.append(rm)
        lnk[rm] = rm + 1
        for t in tmp:
            lnk[t] = rm + 1
    return answer

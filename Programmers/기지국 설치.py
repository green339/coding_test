# https://school.programmers.co.kr/learn/courses/30/lessons/12979
from math import ceil


def solution(n, stations, w):
    answer = 0
    no_electric = [[1, n]]  # 전파가 전달 X 부분
    for s in stations:
        if no_electric:
            a, b = no_electric.pop()
            if s - w - 1 >= a:
                no_electric.append([a, s - w - 1])
            if s + w + 1 <= b:
                no_electric.append([s + w + 1, b])
        else:
            break
    for s, e in no_electric:
        answer += ceil((e - s + 1) / (2 * w + 1))
    return answer


def solution_v2(n, stations, w):
    answer = 0
    s = len(stations)
    si = 0
    pos = 1
    while pos <= n:
        if si < s and pos >= stations[si] - w:
            pos = stations[si] + w + 1
            si += 1
        else:  # 기지국 설치
            answer += 1
            pos += 2 * w + 1
    return answer

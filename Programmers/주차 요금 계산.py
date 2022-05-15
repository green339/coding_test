# https://programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict
import math


def to_time(time):
    time = list(map(int, time.split(':')))
    return time[0] * 60 + time[1]


def solution(fees, records):
    answer = []
    car = defaultdict(list)
    for r in records:
        r = r.split()
        r[0] = to_time(r[0])
        if r[2] == 'IN':
            car[r[1]].append(-r[0])
        else:
            car[r[1]].append(r[0])
    last = to_time('23:59')
    for k, v in sorted(car.items()):
        total = sum(v)
        if len(v) % 2:
            total += last
        cost = total - fees[0]
        if cost > 0:
            answer.append(fees[1] + math.ceil(cost / fees[2]) * fees[3])
        else:
            answer.append(fees[1])
    return answer

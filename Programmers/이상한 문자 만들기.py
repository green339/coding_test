# https://programmers.co.kr/learn/courses/30/lessons/12930
from collections import deque


def solution(s):
    s = deque(s.split(" "))
    answer = []
    while s:
        x = s.popleft()
        tmp = ''
        for i in range(len(x)):
            if i % 2:
                tmp += x[i].lower()
            else:
                tmp += x[i].upper()
        answer.append(tmp)
    return ' '.join(answer)

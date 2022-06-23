# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = []
    sqrt = {"S": 1, "D": 2, "T": 3}
    tmp = ''
    for d in dartResult:
        if d.isnumeric():
            tmp += d
        elif d == "*":
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif d == "#":
            answer[-1] *= -1
        else:
            answer.append(int(tmp) ** sqrt[d])
            tmp = ''
    return sum(answer)


import re


def solution_v2(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    answer = []
    for d in dart:
        if d[2] == '*' and answer:
            answer[-1] *= 2
        answer.append(int(d[0]) ** bonus[d[1]] * option[d[2]])
    return sum(answer)

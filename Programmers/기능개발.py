# https://programmers.co.kr/learn/courses/30/lessons/42586
import math


def solution(progresses, speeds):
    prior = 0
    answer = []
    for p, s in zip(progresses, speeds):
        temp = math.ceil((100 - p) / s)
        if temp <= prior:
            answer[-1] += 1
        else:
            answer.append(1)
            prior = temp
    return answer



def solution_v2(progresses, speeds):
    answer = []
    temp = 0
    for p, s in zip(progresses, speeds):
        cost = math.ceil((100 - p) / s)
        if temp:
            if temp >= cost:
                answer[-1] += 1
        else:
            answer.append(1)
            temp = cost
    return answer

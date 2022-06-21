# https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

from collections import deque


def solution(s):
    s = deque(s)
    stack = []
    while s:
        e = s.popleft()
        if stack and e == stack[-1]:
            stack.pop()
        else:
            stack.append(e)

    return 0 if stack else 1


def solution_v2(s):
    answer = []
    for i in s:
        if answer and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
    return int(not answer)

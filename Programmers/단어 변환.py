# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from collections import deque


def oneDifferent(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return True if diff == 1 else False


def solution(begin, target, words):
    answer = 0
    l = len(words)
    visited = [0] * l
    q = deque()
    q.append((begin, 0))
    while q:
        x, cnt = q.popleft()
        for i in range(l):
            if not visited[i] and oneDifferent(x, words[i]):
                visited[i] = 1
                q.append((words[i], cnt + 1))
                if words[i] == target:
                    return cnt + 1
    return 0

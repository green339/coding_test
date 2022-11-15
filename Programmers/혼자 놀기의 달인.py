# https://school.programmers.co.kr/learn/courses/30/lessons/131130
from collections import deque


def solution(cards):
    answer = []
    visited = [0] * len(cards)
    for i in range(len(cards)):
        if not visited[i]:
            x = cards[i] - 1
            group = set()
            group.add(x)
            while True:
                nx = cards[x] - 1
                if visited[nx]:
                    break
                else:
                    x = nx
                    visited[x] = 1
                    group.add(x)
            answer.append(len(group))
    answer.sort(reverse=True)
    return 0 if len(answer) == 1 else answer[0] * answer[1]

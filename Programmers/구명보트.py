# https://programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution(people, limit):
    people = deque(sorted(people))
    answer = 0
    while len(people) > 1:
        if people[-1] + people[0] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        else:
            people.pop()
            answer += 1
    if people:
        answer += 1
    return answer

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


def solution_v2(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1
    return answer

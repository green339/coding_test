# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict


def dfs(city):
    while airport.get(city, []):
        dfs(airport[city].pop())
    if not airport.get(city, []):
        answer.append(city)


def solution(tickets):
    global airport
    airport = defaultdict(list)
    global answer
    answer = []
    for a, b in tickets:
        airport[a].append(b)
    airport = dict(map(lambda x: (x[0], sorted(x[1], reverse=True)), airport.items()))
    dfs("ICN")
    return answer[::-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations


def check(users, bans):
    for a, b in zip(users, bans):
        if len(a) != len(b):
            return False
        for i, j in zip(a, b):
            if j == '*':
                continue
            if i != j:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    for p in permutations(user_id, len(banned_id)):
        if check(p, banned_id) and set(p) not in answer:
            answer.append(set(p))
    return len(answer)

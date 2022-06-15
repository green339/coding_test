# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    temp = 0
    d = {}
    for p in participant:
        d[hash(p)] = p
        temp += int(hash(p))
    for c in completion:
        temp -= hash(c)
    return d[temp]


def solution_v2(participant, completion):
    c = Counter(participant) - Counter(completion)
    return list(c.keys())[0]


from collections import Counter

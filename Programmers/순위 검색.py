# https://school.programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict


def solution(info, query):
    answer = []
    people = defaultdict(list)
    for i in info:
        i = i.split(" ")
        for language in [i[0], "-"]:
            for job in [i[1], "-"]:
                for career in [i[2], "-"]:
                    for food in [i[3], "-"]:
                        people[language + job + career + food].append(int(i[4]))
    for k in people.keys():
        people[k].sort()
    for q in query:
        q = q.replace(" and ", "")
        q, score = q.split(" ")
        score = int(score)
        l = len(people[q])
        if l == 0:
            answer.append(0)
            continue
        idx = l
        left, right = 0, l - 1
        while left <= right:
            mid = (left + right) // 2
            if people[q][mid] >= score:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        answer.append(l - idx)

    return answer

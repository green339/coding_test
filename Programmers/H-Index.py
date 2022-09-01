# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for cnt, h in enumerate(citations):
        if cnt >= h:
            return cnt
    return len(citations)


def solution_v2(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))


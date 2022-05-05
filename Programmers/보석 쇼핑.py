# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict


def solution(gems):
    answer = []
    l = len(gems)
    cnt = len(set(gems))
    start = 0
    end = 0
    temp = defaultdict(int)
    temp[gems[0]] += 1
    while start <= end:
        if len(temp.keys()) == cnt:
            if end - start < l:
                answer = [start + 1, end + 1]
                l = end - start
            temp[gems[start]] -= 1
            if not temp[gems[start]]:
                del temp[gems[start]]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            temp[gems[end]] += 1

    return answer

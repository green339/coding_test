# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    answer = 0
    cur = 0
    wait = []
    for js, jt in sorted(jobs):
        while wait and cur < js:
            ct, cs = heapq.heappop(wait)
            if cur >= cs:
                answer += cur - cs
                cur += ct
            else:
                answer -= cs - cur
                cur = cs + ct
        heapq.heappush(wait, [jt, js])
    while wait:
        ct, cs = heapq.heappop(wait)
        if cur >= cs:
            answer += cur - cs
            cur += ct
        else:
            answer -= cs - cur
            cur = cs + ct

    return (answer + cur) // len(jobs)

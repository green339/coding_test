# https://school.programmers.co.kr/learn/courses/30/lessons/12927
import heapq


def solution(n, works):
    answer = 0
    hq = []
    for w in works:
        heapq.heappush(hq, -w)
    cnt = 0
    while hq and cnt < n:
        x = heapq.heappop(hq)
        if x < -1:
            heapq.heappush(hq, x + 1)
        cnt += 1
    for t in hq:
        answer += t ** 2
    return answer

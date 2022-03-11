# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    while len(scoville) > 1 and scoville[0] < K:
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + 2 * y)
        answer += 1
    return answer if scoville[0] >= K else -1

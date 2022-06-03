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


def solution_v2(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    x = heapq.heappop(scoville)
    while x < K:
        if scoville:
            y = heapq.heappop(scoville)
            x = heapq.heappushpop(scoville, x + 2 * y)
        else:
            answer = -1
            break
        answer += 1
    return answer

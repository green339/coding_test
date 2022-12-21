# https://school.programmers.co.kr/learn/courses/30/lessons/138477
import heapq
def solution(k, score):
    answer = []
    hq=[]
    for idx,s in enumerate(score):
        if idx<k:
            heapq.heappush(hq,s)
        else:
            if hq[0]<s:
                heapq.heappop(hq)
                heapq.heappush(hq,s)
        answer.append(hq[0])
    return answer
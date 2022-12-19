# https://school.programmers.co.kr/learn/courses/30/lessons/142085
import heapq
def solution(n, k, enemy):
    answer = 0
    q=[]
    for e in enemy:
        heapq.heappush(q,e)
        answer+=1
        if answer<=k:
            continue
        if q[0]<=n:
            n-=heapq.heappop(q)
        else:
            answer-=1
            break
    return answer
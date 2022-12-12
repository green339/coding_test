# https://school.programmers.co.kr/learn/courses/30/lessons/138476
from collections import Counter
def solution(k, tangerine):
    answer = 0
    for v in sorted(Counter(tangerine).values(),reverse=True):
        k-=v
        answer+=1
        if k<=0:
            break
    return answer
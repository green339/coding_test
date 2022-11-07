# https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import defaultdict
def solution(topping):
    answer = 0
    brother=set()
    chul=set(topping)
    kinds=defaultdict(int)
    for t in topping:
        kinds[t]+=1
    for tmp in topping:
        brother.add(tmp)
        kinds[tmp]-=1
        if not kinds[tmp]:
            chul.remove(tmp)
        if len(brother)==len(chul):
            answer+=1
    return answer
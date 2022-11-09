# https://school.programmers.co.kr/learn/courses/30/lessons/131705
from itertools import combinations
def solution (number) :
    answer = 0
    for c in combinations(number,3) :
        if not sum(c):
            answer+=1
    return answer
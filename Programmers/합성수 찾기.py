# https://school.programmers.co.kr/learn/courses/30/lessons/120846
def solution(n):
    answer=0
    for i in range(4,n+1):
        for j in range(2,i):
            if not i%j:
                answer+=1
                break
    return answer
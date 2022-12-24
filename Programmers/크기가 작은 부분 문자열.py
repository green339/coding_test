# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    n=len(t)
    m=len(p)
    p=int(p)
    for i in range(n-m+1):
        if p>=int(t[i:i+m]):
            answer+=1
    return answer
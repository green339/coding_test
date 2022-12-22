# https://school.programmers.co.kr/learn/courses/30/lessons/140108
def solution(s):
    answer = 0
    x="A"
    a,b=0,0
    for cur in s:
        if x=="A":
            x=cur
            a=1
            b=0
            continue
        if cur!=x:
            b+=1
        else:
            a+=1
        if a==b:
            answer+=1
            x="A"
    if x!="A":
        answer+=1
    return answer
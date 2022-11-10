# https://school.programmers.co.kr/learn/courses/30/lessons/133501
def solution(distance, scope, times):
    route=[-1]*(distance+1)
    for idx,s in enumerate(scope):
        s.sort()
        for r in range(s[0],s[1]+1):
            route[r]=idx
    move=0
    while move<distance:
        if route[move]==-1:
            move+=1
        else:
            work,rest=times[route[move]]
            res=move%(work+rest)
            if res and res<=work:
                break
            else:
                move+=1
    return move
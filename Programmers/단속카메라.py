# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    camera = -30001
    for s, e in routes:
        if camera < s:
            answer += 1
            camera = e
    return answer

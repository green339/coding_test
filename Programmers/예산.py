# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d = sorted(d)
    while True:
        if sum(d) > budget:
            d.pop()
        else:
            break
    return len(d)

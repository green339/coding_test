# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = [0, n * m]
    while n != 0:
        r = m % n
        m = n
        n = r
    answer[0] = m
    answer[1] //= m
    return answer

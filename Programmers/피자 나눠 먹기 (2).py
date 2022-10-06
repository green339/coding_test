# https://school.programmers.co.kr/learn/courses/30/lessons/120815
def solution(n):
    for i in range(1, n + 1):
        if not 6 * i % n:
            return i
    return n

# https://school.programmers.co.kr/learn/courses/30/lessons/120909
def solution(n):
    return abs(int(n ** 0.5 % 1 == 0) - 2)

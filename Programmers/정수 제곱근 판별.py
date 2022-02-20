# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    s = int(n ** 0.5)
    return (s + 1) ** 2 if s ** 2 == n else -1

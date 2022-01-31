# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    if a > b:
        a, b = b, a
    return a + b * (b + 1) / 2 - a * (a + 1) / 2

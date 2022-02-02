# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for x in range(1, n):
        if n % x == 1:
            return x

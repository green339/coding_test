# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    return not (x % (sum(map(int, str(x)))))

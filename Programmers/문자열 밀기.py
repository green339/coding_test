# https://school.programmers.co.kr/learn/courses/30/lessons/120921
from collections import deque


def solution(A, B):
    A = deque(A)
    B = deque(B)
    for i in range(len(A) + 1):
        if A == B:
            return i
        A.rotate(1)
    return -1

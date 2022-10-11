# https://school.programmers.co.kr/learn/courses/30/lessons/120878
import math


def solution(a, b):
    b //= math.gcd(a, b)
    while math.gcd(b, 10) != 1:
        if not b % 5:
            b //= 5
        if not b % 2:
            b //= 2
    return 1 if b == 1 else 2

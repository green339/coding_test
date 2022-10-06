# https://school.programmers.co.kr/learn/courses/30/lessons/120840
import math


def solution(balls, share):
    return math.factorial(balls) / (math.factorial(balls - share) * math.factorial(share))

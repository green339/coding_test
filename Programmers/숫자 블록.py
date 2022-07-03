# https://programmers.co.kr/learn/courses/30/lessons/12923
import math


def max_divide(n):
    if n == 1:
        return 0
    result = 1
    s = max(2, math.ceil(n / 10000000))
    e = int(n ** 0.5) + 1
    for i in range(s, e):
        if not n % i:
            result = n // i
            break
    return result


def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(max_divide(i))
    return answer

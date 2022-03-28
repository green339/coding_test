# https://programmers.co.kr/learn/courses/30/lessons/12985
import math


def solution(n, a, b):
    answer = 1
    a, b = min(a, b), max(a, b)
    if a <= n // 2 and b > n // 2:
        return bin(n).count("0") - 1
    while b - a > 1 or b % 2 != 0:
        answer += 1
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
    return answer
# 트리와 비트로 고려 (풀이참고)
#    return ((a-1)^(b-1)).bit_length()

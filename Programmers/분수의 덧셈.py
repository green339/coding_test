# https://school.programmers.co.kr/learn/courses/30/lessons/120808
import math


def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    last = min(denum, num)
    i = math.gcd(denum, num)
    for i in range(last, 0, -1):
        if denum % i == 0 and num % i == 0:
            break
    return [denum // i, num // i]
셈
# https://programmers.co.kr/learn/courses/30/lessons/62048

## 방정식 높이차를 이용한 풀이
import math
def solution(w, h):
    # 방정식 -> y=-(h/w)*x+h
    answer = w * h
    # if w==h:
    #     return answer-w
    if h == 1:
        return 0
    for x in range(w):
        answer -= math.ceil(h * (x + 1) / w) - math.floor(h * x / w)
    return answer


## 최대공약수를 이용한 풀이
def gcd(a, b):
    if (a == 0):
        return b
    else:
        return gcd(b % a, a)


def solution(w, h):
    g = gcd(w, h)
    answer = w * h - (w / g + h / g - 1) * g
    return answer

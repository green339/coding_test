# https://school.programmers.co.kr/learn/courses/30/lessons/120890
def solution(array, n):
    return sorted(array, key=lambda x: (abs(n - x), x))[0]

# https://school.programmers.co.kr/learn/courses/30/lessons/120897
def solution(n):
    return [i for i in range(1, n + 1) if not n % i]

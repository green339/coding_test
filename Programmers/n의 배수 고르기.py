# https://school.programmers.co.kr/learn/courses/30/lessons/120905
def solution(n, numlist):
    return [i for i in numlist if not i%n]
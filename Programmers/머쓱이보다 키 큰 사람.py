# https://school.programmers.co.kr/learn/courses/30/lessons/120585
def solution(array, height):
    return sum([1 for h in array if h > height])

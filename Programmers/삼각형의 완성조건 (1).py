# https://school.programmers.co.kr/learn/courses/30/lessons/120889
def solution(sides):
    return abs(int(2*max(sides)<sum(sides))-2)
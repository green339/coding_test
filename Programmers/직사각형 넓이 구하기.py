# https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    dots.sort()
    return (dots[1][1] - dots[0][1]) * (dots[2][0] - dots[0][0])

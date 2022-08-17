# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    a, b = 0, 0
    for s in sizes:
        w, h = sorted(s)
        a = max(a, w)
        b = max(b, h)
    return a * b


def solution_v2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

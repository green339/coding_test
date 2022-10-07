# https://school.programmers.co.kr/learn/courses/30/lessons/120875
def solution(dots):
    def gradient(a, b):
        if a[0] == b[0]:
            return "divide 0"
        return (a[1] - b[1]) / (a[0] - b[0])

    if gradient(dots[0], dots[1]) == gradient(dots[2], dots[3]):
        return 1
    if gradient(dots[0], dots[2]) == gradient(dots[1], dots[3]):
        return 1
    if gradient(dots[0], dots[3]) == gradient(dots[1], dots[2]):
        return 1
    return 0

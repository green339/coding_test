# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    s = brown + yellow
    sum_w_h = brown / 2 + 2
    for h in range(1, int(s ** 0.5) + 1):
        if not s % h:
            w = s // h
            if w + h == sum_w_h:
                print(w, h)
                return w, h


def solution_v2(brown, yellow):
    for y in range(1, int(yellow ** 0.5) + 1):
        if not yellow % y:
            if brown == 4 + (y + yellow // y) * 2:
                break
    return [yellow // y + 2, y + 2]

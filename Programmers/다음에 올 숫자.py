# https://school.programmers.co.kr/learn/courses/30/lessons/120924
def solution(common):
    if common[2] + common[0] == 2 * common[1]:
        return 2 * common[-1] - common[-2]
    else:
        return common[-1] * common[-1] // common[-2]

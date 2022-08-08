# https://school.programmers.co.kr/learn/courses/30/lessons/12920
def solution(n, cores):
    l = len(cores)
    if l >= n:
        return n
    n -= l
    left = 0
    right = max(cores) * n
    while left < right:
        mid = (left + right) // 2
        tmp = 0
        for c in cores:
            tmp += mid // c
        if tmp >= n:
            right = mid
        else:
            left = mid + 1

    for c in cores:
        n -= (right - 1) // c

    for i in range(l):
        if not right % cores[i]:
            n -= 1
            if not n:
                return i + 1

# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = 0
    n = len(a)
    left_min = [x for x in a]
    right_min = [x for x in a]
    for i in range(1, n):
        left_min[i] = min(left_min[i], left_min[i - 1])
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i], right_min[i + 1])
    for i in range(n):
        if left_min[i] < a[i] and right_min[i] < a[i]:
            continue
        answer += 1
    return answer

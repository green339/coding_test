# https://school.programmers.co.kr/learn/courses/30/lessons/12906
from collections import deque


def solution(arr):
    arr = deque(arr)
    answer = []
    tmp = -1
    while arr:
        x = arr.popleft()
        if tmp == x:
            continue
        else:
            tmp = x
            answer.append(x)
    return answer


def solution_v2(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    return answer

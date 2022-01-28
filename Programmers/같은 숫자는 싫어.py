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

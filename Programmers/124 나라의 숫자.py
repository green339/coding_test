# https://programmers.co.kr/learn/courses/30/lessons/12899
from collections import deque


def solution(n):
    nums = ["1", "2", "4"]
    answer = deque()
    while n:
        n -= 1
        answer.appendleft(nums[n % 3])
        n //= 3

    return ''.join(answer)

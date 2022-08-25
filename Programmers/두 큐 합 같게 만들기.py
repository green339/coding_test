# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque


def solution(queue1, queue2):
    answer = 0
    todo = (sum(queue1) + sum(queue2)) / 2
    one = sum(queue1)
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    while dq1 and dq2:
        if one == todo:
            return answer
        answer += 1
        if one > todo:
            one -= dq1.popleft()
        else:
            dq1.append(dq2.popleft())
            one += dq1[-1]
    return -1


# 투포인터
def solution_v2(queue1, queue2):
    answer = 0
    q = queue1 + queue2
    target = sum(q) / 2
    left = 0
    right = len(queue1) - 1
    cur = sum(queue1)
    while right <= len(q):
        if cur == target:
            return answer
        answer += 1
        if cur > target:
            cur -= q[left]
            left += 1
        else:
            right += 1
            if right < len(q):
                cur += q[right]
    return -1

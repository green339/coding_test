# https://programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque


def solution(s):
    pair = {")": "(", "}": "{", "]": "["}
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1)
        stack = []
        for e in s:
            if e not in pair.keys():
                stack.append(e)
            else:
                if stack and pair[e] == stack[-1]:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
    return answer

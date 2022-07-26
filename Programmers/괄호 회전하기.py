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


def solution_v2(s):
    answer = 0
    n = len(s)
    pair = {')': '(', ']': '[', '}': '{'}
    for start in range(n):
        stack = []
        for x in range(n):
            idx = (x + start) % n
            if s[idx] not in pair.keys():
                stack.append(s[idx])
            else:
                if stack and pair[s[idx]] == stack[-1]:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
    return answer

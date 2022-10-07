# https://school.programmers.co.kr/learn/courses/30/lessons/120853
def solution(s):
    stack = []
    for i in s.split():
        if i == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)

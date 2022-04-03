# https://programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    stack = 0
    for i in s:
        if i == "(":
            stack += 1
        else:
            if stack > 0:
                stack -= 1
            else:
                break
    else:
        return not stack
    return False

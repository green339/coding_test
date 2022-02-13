# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = 0
    for i in s:
        if i.lower() == "y":
            answer += 1
        elif i.lower() == "p":
            answer -= 1
    return not answer

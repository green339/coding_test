# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    l = len(s)
    mid = l // 2
    if not l % 2:
        return s[mid - 1] + s[mid]
    else:
        return s[mid]

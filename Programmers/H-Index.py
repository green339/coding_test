# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for cnt, h in enumerate(citations):
        if cnt >= h:
            return cnt
    return len(citations)

# https://school.programmers.co.kr/learn/courses/30/lessons/120835
def solution(emergency):
    return [sorted(emergency,reverse=True).index(e)+1 for e in emergency]
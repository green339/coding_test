# https://school.programmers.co.kr/learn/courses/30/lessons/120848
def solution(n):
    answer = 0
    while n > answer:
        answer += 1
        n //= answer
    return answer

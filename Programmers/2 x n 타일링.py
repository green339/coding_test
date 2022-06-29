# https://programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    tmp = 1
    answer = 2
    for i in range(3, n + 1):
        tmp, answer = answer, (answer + tmp) % 1000000007
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    tmp = 1
    answer = 2
    for i in range(3, n + 1):
        tmp, answer = answer, (tmp + answer) % 1234567
    return answer if n > 1 else 1

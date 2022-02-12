# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    sqrt = n ** 0.5
    for i in range(1, int(sqrt) + 1):
        if not n % i:
            answer += (i + n // i)
    if int(sqrt) == sqrt:
        answer -= sqrt
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    memo = [0] * (n + 1)
    memo[0] = 1
    for m in money:
        for i in range(1, n + 1):
            if i >= m:
                memo[i] += memo[i - m]
    return memo[-1]

# https://programmers.co.kr/learn/courses/30/lessons/42895
from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    if b:
                        dp[i].add(a // b)
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
        if number in dp[i]:
            break
    else:
        return -1
    return i


def solution_v2(N, number):
    dp = [set() for _ in range(9)]
    for cnt in range(1, 9):  # N 사용횟수
        dp[cnt].add(int(str(N) * cnt))
        for i in range(1, cnt):
            for x in dp[i]:
                for y in dp[cnt - i]:
                    if y:
                        dp[cnt].add(x // y)
                    dp[cnt].add(x + y)
                    dp[cnt].add(x - y)
                    dp[cnt].add(x * y)
        if number in dp[cnt]:
            return cnt
    return -1

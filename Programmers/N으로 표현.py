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

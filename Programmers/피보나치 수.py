# https://programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[-1] % 1234567

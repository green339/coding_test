# https://school.programmers.co.kr/learn/courses/30/lessons/12902
def solution(n):
    dp = [0] * (n // 2 + 1)  # 짝수만
    dp[0] = 1
    dp[1] = 3
    for i in range(2, n // 2 + 1):
        tmp = 0  # ㅣㅡㅡㅡ...ㅡㅡㅣ 인경우
        for j in range(i - 1):
            tmp += dp[j]
        dp[i] = (3 * dp[i - 1] + 2 * tmp) % 1000000007
    return dp[-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    def divisor(num):
        cnt = int(num ** 0.5 % 1 - 1)  # 제곱수 판별
        for i in range(1, int(num ** 0.5) + 1):
            if not num % i:
                cnt += 2
            if cnt > limit:
                return power
        return cnt

    answer = 0
    for n in range(1, number + 1):
        answer += divisor(n)
    return answer

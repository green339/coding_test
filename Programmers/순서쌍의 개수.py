# https://school.programmers.co.kr/learn/courses/30/lessons/120836
def solution(n):
    answer = -int(n ** 0.5 % 1 == 0)
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            answer += 2
    return answer

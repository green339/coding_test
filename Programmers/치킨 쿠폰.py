# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    answer = 0
    while chicken // 10:
        q, r = divmod(chicken, 10)
        answer += q
        chicken = q + r
    return answer

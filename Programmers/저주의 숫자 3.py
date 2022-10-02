# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while '3' in str(answer) or not answer % 3:
            answer += 1
    return answer

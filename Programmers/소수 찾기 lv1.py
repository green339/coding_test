# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if not i % j:
                break
        else:
            answer += 1
    return answer

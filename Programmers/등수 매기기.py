# https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score):
    l = len(score)
    answer = [0] * l
    avg = [(sum(score[i]) / 2, i) for i in range(l)]
    avg.sort(reverse=True)
    prior = 0
    grade = 0
    for i in range(l):
        if prior != avg[i][0]:
            grade = i + 1
            prior = avg[i][0]
        answer[avg[i][1]] = grade
    return answer

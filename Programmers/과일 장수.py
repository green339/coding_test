# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def solution(k, m, score):
    answer = 0
    n=len(score)
    score.sort()
    for i in range(n-m,-1,-m):
        answer+=m*score[i]
    return answer
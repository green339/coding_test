# https://school.programmers.co.kr/learn/courses/30/lessons/120904
def solution(num, k):
    answer = str(num).find(str(k))
    return answer if answer == -1 else answer + 1

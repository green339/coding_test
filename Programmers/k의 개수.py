# https://school.programmers.co.kr/learn/courses/30/lessons/120887
def solution(i, j, k):
    return ' '.join([str(num) for num in range(i, j + 1)]).count(str(k))

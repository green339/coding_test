# https://school.programmers.co.kr/learn/courses/30/lessons/120923
def solution(num, total):
    start = total // num - (num - 1) // 2
    return [i for i in range(start, start + num)]

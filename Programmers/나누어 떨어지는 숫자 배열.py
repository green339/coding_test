# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for a in arr:
        if not a % divisor:
            answer.append(a)
    return sorted(answer) if answer else [-1]

# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    for i in range(500):
        if num == 1:
            break
        if num % 2:
            num = num * 3 + 1
        else:
            num //= 2
    else:
        return -1
    return i

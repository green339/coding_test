# https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    ones = bin(n).count("1")
    while True:
        n += 1
        if bin(n).count("1") == ones:
            break
    return n

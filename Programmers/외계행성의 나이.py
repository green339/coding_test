# https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    return ''.join([chr(int(i) + 97) for i in str(age)])

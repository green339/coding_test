# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for e in s:
        tmp = ord(e)
        if tmp == 32:
            answer += e
        elif tmp >= 97:
            answer += chr((tmp - 97 + n) % 26 + 97)
        else:
            answer += chr((tmp - 65 + n) % 26 + 65)
    return answer

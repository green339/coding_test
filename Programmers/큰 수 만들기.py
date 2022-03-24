# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = []
    for x in number:
        while k > 0 and answer and answer[-1] < x:
            answer.pop()
            k -= 1
        answer.append(x)
    return ''.join(answer[:len(number) - k])
# 스택풀이

# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = []
    sqrt = {"S": 1, "D": 2, "T": 3}
    tmp = ''
    for d in dartResult:
        if d.isnumeric():
            tmp += d
        elif d == "*":
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif d == "#":
            answer[-1] *= -1
        else:
            answer.append(int(tmp) ** sqrt[d])
            tmp = ''
    return sum(answer)

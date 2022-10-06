# https://school.programmers.co.kr/learn/courses/30/lessons/120863
def solution(polynomial):
    polynomial = polynomial.split(" + ")
    res = [0, 0]
    for p in polynomial:
        if p.isdigit():
            res[1] += int(p)
        else:
            p = p[:-1]
            if not p:
                res[0] += 1
            else:
                res[0] += int(p)
    answer = ""
    if res[0]:
        if res[0] == 1:
            answer += "x"
        else:
            answer += str(res[0]) + "x"
        if res[1]:
            answer += " + " + str(res[1])
    else:
        answer += str(res[1])
    return answer

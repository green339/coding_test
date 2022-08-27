# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def separate(p):
    u = ''
    v = ''
    left = 0
    for i in range(0, len(p)):
        u += p[i]
        if p[i] == "(":
            left += 1
        if left == i - left + 1:
            v += p[i + 1:]
            break
    return u, v


def solution(p):
    answer = ''
    u, v = separate(p)
    if len(p) > 0:
        if u[0] == "(" and u[-1] == ")":
            v = solution(v)
            answer = u + v
        else:
            v = solution(v)
            answer = '(' + v + ')'
            for i in u[1:-1]:
                if i == "(":
                    answer += ')'
                elif i == ')':
                    answer += '('
    return answer

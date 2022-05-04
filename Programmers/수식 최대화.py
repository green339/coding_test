# https://programmers.co.kr/learn/courses/30/lessons/67257
def solution(expression):
    answer = 0
    op = [("+", "*", "-"), ("+", "-", "*"), ("*", "+", "-"), ("*", "-", "+"), ("-", "*", "+"), ("-", "+", "*")]

    for o in op:
        first = o[0]
        second = o[1]
        a = []
        for e in expression.split(first):
            b = []
            for k in e.split(second):
                b.append(str(eval(k)))
            a.append(str(eval(second.join(b))))
        temp = eval(first.join(a))
        answer = max(answer, abs(temp))
    return answer


def solution_v2(expression):
    answer = 0
    oplist = [['+', '-'], ['+', '*'], ['-', '+'], ['-', '*'], ['*', '+'], ['*', '-']]
    for a, b in oplist:
        temp1 = []
        for e1 in expression.split(a):
            temp2 = []
            for e2 in e1.split(b):
                temp2.append(str(eval(e2)))
            temp1.append(str(eval(b.join(temp2))))
        answer = max(answer, abs(eval(a.join(temp1))))

    return answer

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

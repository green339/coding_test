# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    answer = []
    numbers=set(X)&set(Y)
    for n in sorted(list(numbers),reverse=True):
        for _ in range (min(X.count(n),Y.count(n))):
            answer.append(n)
    if not answer:
        return "-1"
    if int(answer[0])==0:
        return "0"
    return ''.join(answer)
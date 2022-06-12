# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = 0
    three = []
    while n > 2:
        three.append(n % 3)
        n //= 3
    three.append(n)
    for i, x in enumerate(three[::-1]):
        answer += x * (3 ** i)
    return answer


def solution_v2(n):
    nn = ''
    while n:
        n, r = divmod(n, 3)
        nn += str(r)
    answer = int(nn, 3)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    answer = 0
    while n>=a:
        q,n=divmod(n,a)
        n+=q*b
        answer+=q*b
    return answer
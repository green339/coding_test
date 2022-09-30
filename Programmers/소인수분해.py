# https://school.programmers.co.kr/learn/courses/30/lessons/120852
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            return False
    return True

def solution(n):
    answer = []
    for i in range(2,n+1):
        if not n%i and is_prime(i):
            answer.append(i)
    return answer
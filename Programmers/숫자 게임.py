# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] < B[answer]:
            answer += 1
    return answer

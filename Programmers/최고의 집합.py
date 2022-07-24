# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    if s < n:
        return [-1]
    q, r = divmod(s, n)
    answer = [q for _ in range(n)]
    for i in range(1, r + 1):
        answer[-i] += 1
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n
    students = [0] * (n + 1)
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1

    for i in range(1, n + 1):
        if students[i] < 0:
            for di in [-1, 1]:
                ni = i + di
                if 0 < ni < n + 1 and students[ni] > 0:
                    students[i] += 1
                    students[ni] -= 1
                    break
        if students[i] < 0:
            answer -= 1
    return answer

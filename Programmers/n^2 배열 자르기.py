# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right) + 1): # int(left),int(right) 안하면 에러가 남
        answer.append(max(i // n, i % n) + 1)
    return answer

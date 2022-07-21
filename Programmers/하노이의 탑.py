# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    def hanoi(n, start, dest, via):
        if n == 1:
            answer.append([start, dest])
            return
        hanoi(n - 1, start, via, dest)
        answer.append([start, dest])
        hanoi(n - 1, via, dest, start)

    answer = []
    hanoi(n, 1, 3, 2)
    return answer


'''
if n==1: start->dest (종료)
else:
    n-1개 start->via
    1개(n개 원판 중 마지막) start->dest
    n-1개 via->dest
'''

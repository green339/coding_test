# https://www.acmicpc.net/problem/2661
import sys

input = sys.stdin.readline


def check():
    l = len(answer)
    for i in range(1, l // 2 + 1):
        for j in range(l - 1, l - i - 1, -1):
            if answer[j] != answer[j - i]:
                break
        else:
            return False
    return True


def backtracking(cur):
    if cur == n:
        print(''.join(answer))
        exit()
    for i in numbers:
        answer.append(i)
        if check():
            backtracking(cur + 1)
        answer.pop()


n = int(input())
numbers = ['1', '2', '3']
answer = []
backtracking(0)

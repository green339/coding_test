# https://programmers.co.kr/learn/courses/30/lessons/12952

def check(x):
    for i in range(x):
        if board[i] == board[x]:
            return False
        if abs(board[i] - board[x]) == x - i:
            return False
    return True


def dfs(depth):
    global answer
    if depth == l:
        answer += 1
        return
    for i in range(l):
        board[depth] = i
        if check(depth):
            dfs(depth + 1)


def solution(n):
    global board, l, answer
    answer = 0
    l = n
    answer = 0
    board = [0] * n
    dfs(0)
    return answer
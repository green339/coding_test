# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i - 1] == 0:
                continue
            if stack and stack[-1] == board[j][i - 1]:
                stack.pop()
                answer += 2
            else:
                stack.append(board[j][i - 1])
            board[j][i - 1] = 0
            break
    return answer


def solution_v2(board, moves):
    n = len(board)
    answer = 0
    arr = [[] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if board[i][j]:
                arr[j].append(board[i][j])
    stack = []
    for m in moves:
        if arr[m - 1]:
            doll = arr[m - 1].pop()
            if stack and stack[-1] == doll:
                stack.pop()
                answer += 2
            else:
                stack.append(doll)
    return answer

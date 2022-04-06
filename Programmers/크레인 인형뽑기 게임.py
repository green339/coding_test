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

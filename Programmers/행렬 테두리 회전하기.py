# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    board = []
    for i in range(rows):
        board.append([columns * i + j for j in range(1, columns + 1)])
    answer = []
    for qx1, qy1, qx2, qy2 in queries:
        min_num = rows * columns
        qx1 -= 1
        qx2 -= 1
        qy1 -= 1
        qy2 -= 1
        tmp = board[qx1][qy1]
        for y in range(qy1 + 1, qy2):
            min_num = min(tmp, min_num)
            board[qx1][qy1] = board[qx1][y]
            board[qx1][y] = tmp
            tmp = board[qx1][qy1]

        for x in range(qx1, qx2):
            min_num = min(tmp, min_num)
            board[qx1][qy1] = board[x][qy2]
            board[x][qy2] = tmp
            tmp = board[qx1][qy1]

        for y in range(qy2, qy1, -1):
            min_num = min(tmp, min_num)
            board[qx1][qy1] = board[qx2][y]
            board[qx2][y] = tmp
            tmp = board[qx1][qy1]

        for x in range(qx2, qx1, -1):
            min_num = min(tmp, min_num)
            board[qx1][qy1] = board[x][qy1]
            board[x][qy1] = tmp
            tmp = board[qx1][qy1]
        answer.append(min(min_num, tmp))
    return answer

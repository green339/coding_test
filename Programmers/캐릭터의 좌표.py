# https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    d = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    r = board[0] // 2
    c = board[1] // 2
    x = 0
    y = 0
    for key in keyinput:
        nx = x + d[key][0]
        ny = y + d[key][1]
        if -r <= nx <= r and -c <= ny <= c:
            x = nx
            y = ny
    return [x, y]

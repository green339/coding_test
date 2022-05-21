# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    visited = [[[0, 0] for _ in range(11)] for _ in range(11)]
    x = 5
    y = 5
    for d in dirs:
        if d == 'U':
            if x == 0:
                continue
            x -= 1
            if not visited[x][y][1]:
                visited[x][y][1] = 1
                answer += 1
        elif d == 'D':
            if x == 10:
                continue
            if not visited[x][y][1]:
                visited[x][y][1] = 1
                answer += 1
            x += 1
        elif d == 'L':
            if y == 0:
                continue
            y -= 1
            if not visited[x][y][0]:
                visited[x][y][0] = 1
                answer += 1
        elif d == 'R':
            if y == 10:
                continue
            if not visited[x][y][0]:
                visited[x][y][0] = 1
                answer += 1
            y += 1
    return answer

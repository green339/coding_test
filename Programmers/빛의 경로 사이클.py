# https://school.programmers.co.kr/learn/courses/30/lessons/86052
def solution(grid):
    def cycle(sx, sy, sd):
        bd = sd
        if grid[sx][sy] == 'L':
            bd = (bd + 1) % 4
        elif grid[sx][sy] == 'R':
            bd = (bd - 1) % 4
        # 일단 처음에는 쏜 방향대로 직진
        x = (sx + dx[sd]) % r
        y = (sy + dy[sd]) % c
        d = sd
        cost = 1
        while x != sx or y != sy or d != bd:
            if grid[x][y] == 'L':
                d = (d - 1) % 4
            elif grid[x][y] == 'R':
                d = (d + 1) % 4
            visited[x][y][d] = 1
            x = (x + dx[d]) % r
            y = (y + dy[d]) % c
            cost += 1
        return cost

    dx = [0, 1, 0, -1]  # 동서남북
    dy = [1, 0, -1, 0]
    answer = []
    r = len(grid)
    c = len(grid[0])
    visited = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for d in range(4):
                if not visited[i][j][d]:
                    visited[i][j][d] = 1
                    answer.append(cycle(i, j, d))
    return sorted(answer)


## cycle에서 while문 종료조건 변경
def solution(grid):
    def cycle(x, y, d):
        cost = 0
        while not visited[x][y][d]:
            visited[x][y][d] = 1
            d = (d + turn[grid[x][y]]) % 4
            x = (x + dx[d]) % r
            y = (y + dy[d]) % c
            cost += 1
        return cost

    dx = [0, 1, 0, -1]  # 동서남북
    dy = [1, 0, -1, 0]
    turn = {'L': -1, 'R': 1, 'S': 0}
    answer = []
    r = len(grid)
    c = len(grid[0])
    visited = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            for d in range(4):
                if not visited[i][j][d]:
                    answer.append(cycle(i, j, d))
    return sorted(answer)

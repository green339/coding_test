# https://www.acmicpc.net/problem/21609
import sys
from collections import deque

input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 불록을 찾는다.
def find_block():
    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] = 1
        block = set()
        block.add((sx, sy))
        color = board[sx][sy]
        rainbow = 0
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < N and -1 < ny < N:
                    if (nx, ny) not in block and not visited[nx][ny]:
                        if board[nx][ny] == -1:
                            visited[nx][ny] = 1
                        elif board[nx][ny] == color:
                            visited[nx][ny] = 1
                            block.add((nx, ny))
                            q.append((nx, ny))
                        elif board[nx][ny] == 0:
                            block.add((nx, ny))
                            q.append((nx, ny))
                            rainbow += 1
        flag.append([len(block), rainbow, sx, sy])
        groups[(sx, sy)] = block

    global answer
    visited = [[0] * N for _ in range(N)]
    flag = []
    groups = dict()
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] > 0:
                bfs(i, j)
    flag.sort(reverse=True)
    if not flag:
        return False
    if flag[0][0] == 1:
        return False
    for bx, by in groups[(flag[0][2], flag[0][3])]:
        board[bx][by] = -2  # 빈칸
    answer += flag[0][0] ** 2
    return True


def gravity():
    for j in range(N):
        floor = N
        for i in range(N - 1, -1, -1):
            if board[i][j] == -1:
                floor = i
            elif board[i][j] > -1:
                tmp = board[i][j]
                board[i][j] = -2
                board[floor - 1][j] = tmp
                floor -= 1


answer = 0
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
while find_block():
    gravity()
    board = list(map(list, zip(*board)))[::-1]
    gravity()
print(answer)

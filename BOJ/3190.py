# https://www.acmicpc.net/problem/3190
from collections import deque

direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 2  # 사과 위치
D = int(input())
command = deque(list(input().split()) for _ in range(D))
snake_dir = 0
snake = deque()
snake.append((0, 0))
board[0][0] = 1  # 뱀 위치
t = 1
while True:
    nx = snake[0][0] + direction[snake_dir][0]
    ny = snake[0][1] + direction[snake_dir][1]
    if -1 < nx < N and -1 < ny < N and board[nx][ny] != 1:
        snake.appendleft((nx, ny))
        if not board[nx][ny]:
            px, py = snake.pop()
            board[px][py] = 0
        board[nx][ny] = 1
    else:
        break
    if command and int(command[0][0]) == t:
        x, c = command.popleft()
        if c == 'D':
            snake_dir = (snake_dir + 1) % 4
        else:
            snake_dir = (snake_dir - 1) % 4
    t += 1
print(t)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
# 8:55

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(depth, sx, sy, flag, cur):
    global value
    value = max(depth, value)
    for dx, dy in d:
        nx = sx + dx
        ny = sy + dy
        if -1 < nx < N and -1 < ny < N:
            if not visited[nx][ny]:
                if board[nx][ny] < cur:
                    visited[nx][ny] = 1
                    dfs(depth + 1, nx, ny, flag, board[nx][ny])
                    visited[nx][ny] = 0
                else:
                    if flag and board[nx][ny] - cur < K:
                        visited[nx][ny] = 1
                        dfs(depth + 1, nx, ny, 0, cur - 1)
                        visited[nx][ny] = 0


T = int(input())
answer = dict()
for key in range(1, T + 1):
    board = []
    N, K = map(int, input().split())
    max_height = 0
    max_height_loc = []
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(N):
            if board[i][j] > max_height:
                max_height = board[i][j]
                max_height_loc = [(i, j)]
            elif board[i][j] == max_height:
                max_height_loc.append((i, j))
    value = 0
    visited = [[0] * N for _ in range(N)]
    for mx, my in max_height_loc:
        visited[mx][my] = 1
        dfs(1, mx, my, 1, board[mx][my])
        visited[mx][my] = 0
    answer[key] = value

for k, v in answer.items():
    print(f"#{k} {v}", )

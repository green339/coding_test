import sys

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]


def dfs(nx, ny):
    cnt = 1
    for i in range(4):
        vx = nx + dx[i]
        vy = ny + dy[i]
        if -1 < vx < N and -1 < vy < N:
            if board[vx][vy]:
                board[vx][vy] = 0
                cnt += dfs(vx, vy)
    return cnt


if __name__ == "__main__":
    global N
    N = int(input())
    global board
    board = [list(map(int, list(input().strip()))) for _ in range(N)]
    answer = []
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                board[x][y] = 0
                answer.append(dfs(x, y))
    print(len(answer))
    for a in sorted(answer):
        print(a)
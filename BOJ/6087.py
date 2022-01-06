# https://www.acmicpc.net/problem/21608
import sys
from collections import deque

input = sys.stdin.readline
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs():
    q = deque([(laser[0][0], laser[0][1])]) # 회전 횟수 x, y, 방향
    visited[laser[0][0]][laser[0][1]] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in direction: # 북, 동, 남, 서
            nx = x + dx
            ny = y + dy
            while True:
                if -1 < nx < H and -1 < ny < W:
                    if board[nx][ny] == "*": # 벽을 만나는 경우
                        break
                    if visited[nx][ny] < visited[x][y] + 1: # 이전에 더 적은 거울 수로 방문한 경우
                        break
                else: # 범위 밖
                    break
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx += dx
                ny += dy


if __name__ == "__main__":
    W, H = map(int, input().split())
    board = []
    laser = []
    visited = [[10e9] * W for _ in range(H)]
    for i in range(H):
        board.append(list(input().strip()))
        for j, b in enumerate(board[-1]):
            if b == "C":
                laser.append((i, j))
    bfs()
    print(visited[laser[1][0]][laser[1][1]]-1)

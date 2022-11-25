# https://www.acmicpc.net/problem/15686
import sys
input = sys.stdin.readline

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def chicken_distance(sx, sy):
    dist = 2 * N
    for i in range(len(chicken)):
        if visited[i]:
            dist = min(dist, abs(chicken[i][0] - sx) + abs(chicken[i][1] - sy))
    return dist


def dfs(idx, cnt):
    global answer
    if cnt == M:
        cur = 0
        for hx, hy in home:
            cur += chicken_distance(hx, hy)
        if answer > cur:
            answer = cur
        return
    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = 1
            dfs(i + 1, cnt + 1)
            visited[i] = 0


answer = 10e9
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])
            board[i][j] = 0
visited = [0] * len(chicken)
dfs(0, 0)
print(answer)

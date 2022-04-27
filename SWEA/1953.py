# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
import heapq

direction = {1: [(-1, 0), (0, 1), (0, -1), (1, 0)],
             2: [(-1, 0), (1, 0)],
             3: [(0, -1), (0, 1)],
             4: [(-1, 0), (0, 1)],
             5: [(0, 1), (1, 0)],
             6: [(0, -1), (1, 0)],
             7: [(-1, 0), (0, -1)]}

T = int(input())
answer = dict()
for test in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    q = [(0, R, C)]
    visited[R][C] = 1
    while q:
        cost, x, y = heapq.heappop(q)
        if cost >= L-1:
            break
        for dx, dy in direction[board[x][y]]:
            nx = x + dx
            ny = y + dy
            if -1 < nx < N and -1 < ny < M:
                if not visited[nx][ny] and board[nx][ny]:
                    if (-dx,-dy) in direction[board[nx][ny]]:
                        visited[nx][ny] = 1
                        heapq.heappush(q,(cost + 1, nx, ny))
    value = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                value += 1
    answer[test] = value
for k,v in answer.items():
    print(f"#{k} {v}")

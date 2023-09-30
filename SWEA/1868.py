from collections import deque


T = int(input())
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    mine = [[0] * N for _ in range(N)]  # 이웃한 지뢰의 수
    for i in range(N):
        for j in range(N):
            if board[i][j] == ".":
                for di, dj in d:
                    ni = i + di
                    nj = j + dj
                    if -1 < ni < N and -1 < nj < N:
                        if board[ni][nj] == "*":
                            mine[i][j] += 1
            else:
                mine[i][j] = -1
    answer = 0
    # 주변 방문하기- 만약에 0이면 q에 넣고 0초과면 q에 넣지 않는다
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mine[i][j] > -1 and visited[i][j] == 0:
                answer += 1
                q = deque([(i, j)])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx = dx + x
                        ny = dy + y
                        if -1 < nx < N and -1 < ny < N:
                            if mine[nx][ny]==0 and visited[nx][ny] == 0:
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1
                            if mine[x][y] == 0:
                                if mine[nx][ny]>0 and visited[nx][ny]==0:
                                    visited[nx][ny]=1
    print(f"#{test_case} {answer}")
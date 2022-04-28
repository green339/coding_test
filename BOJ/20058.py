# https://www.acmicpc.net/problem/20058
from collections import deque
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs():
    global answer
    cnt = 1
    q = deque()
    q.append((sx, sy))
    while q:
        vx, vy = q.popleft()
        for dx, dy in direction:
            nx = vx + dx
            ny = vy + dy
            if -1 < nx < M and -1 < ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if A[nx][ny]:
                    q.append((nx, ny))
                    cnt += 1
    answer = max(answer, cnt)


def fire_storm():
    block_size = 2 ** stage
    for i in range(0, M, block_size):
        for j in range(0, M, block_size):
            temp = []
            for x in range(block_size):
                temp.append(A[i + x][j:j + block_size])
            for idx, t in enumerate(temp):
                col = block_size - 1 - idx
                for row in range(block_size):
                    A[i + row][j + col] = t[row]

    no_ice = [[0] * M for _ in range(M)]
    for r in range(M):
        for c in range(M):
            if A[r][c]:
                cnt = 0
                for dr, dc in direction:
                    nr = dr + r
                    nc = dc + c
                    if -1 < nr < M and -1 < nc < M and A[nr][nc]:
                        cnt += 1
                if cnt < 3:
                    no_ice[r][c] = -1
    for r in range(M):
        for c in range(M):
            A[r][c] += no_ice[r][c]


N, _ = map(int, input().split())
M = 2 ** N
A = [list(map(int, input().split())) for _ in range(M)]
L = list(map(int, input().split()))
for stage in L:
    fire_storm()
answer = 1
visited = [[0] * M for _ in range(M)]
for sx in range(M):
    for sy in range(M):
        if not visited[sx][sy] and A[sx][sy]:
            visited[sx][sy] = 1
            bfs()
print(sum(map(sum, A)))
print(answer if answer > 1 else 0)

# 처음에 생각한 회전방법 2**L 부분격자로 나눠지면 다시 2**(L-1) 부분격자 단위로 회전한다고 생각함
# 문제에서 주어진 회전방법 -> 2**L 부분격자로 나눠지면 거기서 row1이 col2**L이 되고 row2가 col2**L-1이 되는 식으로 행이 90도 회전
# block_size = int(2 ** (stage - 1))
# for i in range(0, M, 2 ** stage):
#     for j in range(0, M, 2 ** stage):
#         temp = [[0] * block_size * 2 for _ in range(block_size * 2)]
#         for x in range(block_size):
#             for y in range(block_size):
#                 temp[x][y + block_size] = A[i + x][j + y + block_size]
#                 A[i + x][j + y + block_size] = A[i + x][j + y]
#         for x in range(block_size):
#             for y in range(block_size, block_size + block_size):
#                 temp[x + block_size][y] = A[i + x + block_size][j + y]
#                 A[i + x + block_size][j + y] = temp[x][y]
#         for x in range(block_size, block_size + block_size):
#             for y in range(block_size, block_size + block_size):
#                 temp[x][y - block_size] = A[i + x][j + y - block_size]
#                 A[i + x][j + y - block_size] = temp[x][y]
#                 A[i + x - block_size][j + y - block_size] = temp[x][y - block_size]

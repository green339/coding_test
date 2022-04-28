# https://www.acmicpc.net/problem/20056
# 3:26
direction = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
answer = 0
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
visited = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append([m, s, d])
    answer += m

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                while board[i][j]:
                    m, s, d = board[i][j].pop()
                    ni = (i + direction[d][0] * s) % N
                    nj = (j + direction[d][1] * s) % N
                    visited[ni][nj].append([m, s, d])
    for i in range(N):
        for j in range(N):
            if len(visited[i][j]) > 1:
                cnt = len(visited[i][j])
                sum_m = 0
                sum_s = 0
                sum_d = set()
                while visited[i][j]:
                    m, s, d = visited[i][j].pop()
                    sum_m += m
                    sum_s += s
                    sum_d.add(d % 2)
                answer -= sum_m
                if sum_m < 5:
                    continue
                sum_m //= 5
                sum_s //= cnt
                y = len(sum_d) - 1
                for x in range(4):
                    board[i][j].append([sum_m, sum_s, 2 * x + y])
                answer += sum_m * 4
            elif visited[i][j]:
                board[i][j].append(visited[i][j].pop())
print(answer)

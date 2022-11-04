# https://www.acmicpc.net/problem/14889
import sys

input = sys.stdin.readline


def dfs(depth, idx):
    global answer
    if depth == N // 2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(i, N):
                if visited[i] and visited[j]:
                    start += S[i][j] + S[j][i]
                elif not visited[i] and not visited[j]:
                    link += S[i][j] + S[j][i]
        answer = min(answer, abs(start - link))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
answer = 10e9
visited = [0] * N
dfs(0,0)
print(answer)

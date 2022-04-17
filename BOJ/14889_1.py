# https://www.acmicpc.net/problem/14889

import sys
input = sys.stdin.readline


def dfs(depth, idx):
    global answer
    if depth == N // 2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(i,N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                    start += S[j][i]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
                    link += S[j][i]
        answer = min(answer, abs(start - link))
        return

    for x in range(idx, N):
        if not visited[x]:
            visited[x] = 1
            dfs(depth + 1, x + 1)
            visited[x] = 0


if __name__ == "__main__":
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    answer = int(1e9)
    dfs(0, 0)
    print(answer)

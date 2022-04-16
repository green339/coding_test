# https://www.acmicpc.net/problem/16235
import sys
from collections import defaultdict

input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    board = [[5] * N for _ in range(N)]
    A = [list(map(int, input().split())) for _ in range(N)]
    tree = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, input().split())
        tree[x - 1][y - 1][z] += 1

    # 봄 여름 겨울
    for _ in range(K):
        for i in range(N):
            for j in range(N):
                if not tree[i][j]:
                    board[i][j]+=A[i][j]
                    continue
                temp = defaultdict(int)
                die = 0
                for k in sorted(tree[i][j].keys()):
                    survive = min(tree[i][j][k], board[i][j] // k)
                    board[i][j] -= survive * k
                    if survive:
                        temp[k + 1] += survive
                    die += (tree[i][j][k] - survive) * (k // 2)
                board[i][j] += (die + A[i][j])
                tree[i][j] = temp
        # 가을
        for r in range(N):
            for c in range(N):
                if tree[r][c]:
                    cnt = 0
                    for age in tree[r][c].keys():
                        if age % 5 == 0:
                            cnt += tree[r][c][age]
                    if cnt:
                        for d in range(8):
                            nr = dx[d] + r
                            nc = dy[d] + c
                            if -1 < nr < N and -1 < nc < N:
                                tree[nr][nc][1] += cnt
    answer = 0
    for a in range(N):
        for b in range(N):
            if tree[a][b]:
                answer += sum(tree[a][b].values())
    print(answer)


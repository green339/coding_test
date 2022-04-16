# https://www.acmicpc.net/problem/21610
import sys

input = sys.stdin.readline
direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    cloud = {(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)}
    for _ in range(M):
        d, s = map(int, input().split())
        move = set()
        for cx, cy in cloud:
            dx, dy = direction[d]
            move.add(((cx + dx * s) % N, (cy + dy * s) % N))
        for r, c in move:
            A[r][c] += 1
        cloud = set()
        for r, c in move:
            cnt = 0
            for idx in [2, 4, 6, 8]:
                nr = r + direction[idx][0]
                nc = c + direction[idx][1]
                if -1 < nr < N and -1 < nc < N and A[nr][nc]:
                    cnt += 1
            A[r][c] += cnt
        for x in range(N):
            for y in range(N):
                if (x, y) not in move and A[x][y] >= 2:
                    A[x][y] -= 2
                    cloud.add((x, y))
    print(sum(map(sum, A)))

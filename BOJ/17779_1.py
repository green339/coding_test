# https://www.acmicpc.net/problem/17779
import sys

input = sys.stdin.readline


def separate(x, y, d1, d2):
    region = [0, 0, 0, 0, 0]
    for r in range(x):
        region[1] += sum(A[r][:y + 1])
        region[2] += sum(A[r][y + 1:])
    for r in range(x + d1 + d2 + 1, N):
        region[3] += sum(A[r][:y - d1 + d2])
        region[4] += sum(A[r][y - d1 + d2:])

    # 구역1
    for k in range(d1):
        region[1] += sum(A[x + k][:y - k])
    # 구역2
    for k in range(d2 + 1):
        region[2] += sum(A[x + k][y + k + 1:])
    # 구역3
    for k in range(d2 + 1):
        region[3] += sum(A[x + d1 + k][:y - d1 + k])
    # 구역4
    for k in range(1, d1 + 1):
        region[4] += sum(A[x + d2 + k][y + d2 - k + 1:])
    region[0] = total - sum(region)
    return max(region) - min(region)


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
total = sum(map(sum, A))
answer = total
for i in range(N - 2):
    for j in range(N - 1):
        for dd1 in range(1, j + 1):
            for dd2 in range(1, N - j + i):
                if i + dd1 + dd2 >= N:
                    continue
                answer = min(answer, separate(i, j, dd1, dd2))
print(answer)

# https://www.acmicpc.net/problem/17779
from collections import defaultdict


def edge_comb(x, y):
    d = []
    for a in range(1, y):  # d1
        for b in range(1, N - y + 1):  # d2
            if x + a + b > N:
                continue
            d.append([a, b])
    return d


def edge_area(x, y, a, b):
    global edge
    for do in range(a + 1):
        edge[x + do].add(y - do)
        edge[x + b + do].add(y + b - do)
    for dt in range(b + 1):
        edge[x + dt].add(y + dt)
        edge[x + a + dt].add(y - a + dt)


def region(a1, a2, b1, b2, flag):
    area = 0
    n1 = b1
    n2 = b2
    for x in range(a1, a2 + 1):
        if x in edge.keys():
            if flag == 1 or flag == 3:
                n2 = min(min(edge[x]) - 1, b2)
            elif flag == 2 or flag == 4:
                n1 = max(b1, max(edge[x]) + 1)
        else:
            n1 = b1
            n2 = b2
        for y in range(n1, n2 + 1):
            area += A[x][y]
    return area


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

#  범위가 어려울 땐 문제 조건에 맞춰서 범위를 바꿔줌
A.insert(0, [0] * N)
for i in range(N + 1):
    A[i].insert(0, 0)

all_ppl = sum(map(sum, A))
answer = 40000
for i in range(1, N):
    for j in range(1, N):
        ds = edge_comb(i, j)
        for d1, d2 in ds:
            edge = defaultdict(set)
            edge_area(i, j, d1, d2)
            ppl = [0] * 5
            ppl[0] = region(1, i + d1 - 1, 1, j, 1)
            ppl[1] = region(1, i + d2, j + 1, N, 2)
            ppl[2] = region(i + d1, N, 1, j - d1 + d2 - 1, 3)
            ppl[3] = region(i + d2 + 1, N, j - d1 + d2, N, 4)
            ppl[4] = all_ppl - sum(ppl)
            answer = min(max(ppl) - min(ppl), answer)
print(answer)

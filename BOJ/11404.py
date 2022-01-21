# https://www.acmicpc.net/problem/11404
import sys

input = sys.stdin.readline
inf = 10e9

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    city = [[inf] * n for _ in range(n)]
    for x in range(n):
        city[x][x] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        city[a - 1][b - 1] = min(city[a - 1][b - 1], c)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                city[i][j] = min(city[i][j], city[i][k] + city[k][j])
    for c in city:
        for e in c:
            if e == inf:
                print(0, end=' ')
            else:
                print(e, end=' ')
        print()

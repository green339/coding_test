# https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations

input = sys.stdin.readline

if __name__ == "__main__":
    answer = 10e9
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    player = [i for i in range(N)]
    candidate = combinations(player, N // 2)
    for start in candidate:
        link = [j for j in range(N) if j not in start]
        start_a = 0
        link_a = 0
        for x, a in zip(start, link):
            for y, b in zip(start, link):
                start_a += S[x][y]
                link_a += S[a][b]
        answer = min(answer, abs(link_a - start_a))

    print(answer)

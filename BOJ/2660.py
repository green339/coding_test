# https://www.acmicpc.net/problem/2660
import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    friend = [[10e9] * n for _ in range(n)]
    for x in range(n):
        friend[x][x] = 0
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        friend[a - 1][b - 1] = 1
        friend[b - 1][a - 1] = 1
    # 플로이드 와샬
    for k in range(n):
        for i in range(n):
            for j in range(n):
                friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])
    score = defaultdict(list)
    for idx, f in enumerate(friend):
        score[max(f)].append(idx + 1)
    ans_score = min(score.keys())
    print(ans_score, len(score[ans_score]))
    print(*sorted(score[ans_score]))

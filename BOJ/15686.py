# https://www.acmicpc.net/problem/15686
import sys

input = sys.stdin.readline


def city_chicken_distance():
    distance = 0
    for hx, hy in home:
        home_to_chicken = 1e9
        for i in range(chicken_cnt):
            if visited[i]:
                home_to_chicken = min(home_to_chicken, abs(hx - chicken[i][0]) + abs(hy - chicken[i][1]))
        distance += home_to_chicken
    return distance


def dfs(depth, idx):
    global answer
    if depth == M:
        answer = min(answer, city_chicken_distance())
        return
    for i in range(idx, chicken_cnt):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0


N, M = map(int, input().split())
home = []
chicken = []
chicken_cnt = 0
for r in range(N):
    temp = list(map(int, input().split()))
    for c in range(N):
        if temp[c] == 1:
            home.append((r, c))
        elif temp[c] == 2:
            chicken_cnt += 1
            chicken.append((r, c))

visited = [0] * chicken_cnt
answer = 1e9
dfs(0, 0)
print(answer)

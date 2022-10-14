# https://www.acmicpc.net/problem/12100
import sys

input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(depth, arr):
    global answer
    if depth == 5:
        answer = max(answer, max(map(max, arr)))
        return
    for dx, dy in d:
        if dx == 1:  # 아래
            dfs(depth + 1, list(zip(*move(list(zip(*arr[::-1])))))[::-1])
        elif dx == -1:  # 위
            dfs(depth + 1, list(zip(*move(list(zip(*arr))))))
        elif dy == 1:  # 오
            dfs(depth + 1, [k[::-1] for k in move([a[::-1] for a in arr])])
        elif dy == -1:  # 왼
            dfs(depth + 1, move(arr))


def move(arr):
    arr = list(map(list, arr))
    for i in range(N):
        while 0 in arr[i]:
            arr[i].remove(0)
    for i in range(N):
        j = 0
        while j < len(arr[i]) - 1:
            if arr[i][j] == arr[i][j + 1]:
                arr[i][j] += arr[i][j + 1]
                arr[i][j + 1] = 0
                arr[i].remove(0)
            j += 1
        for k in range(N - len(arr[i])):
            arr[i].append(0)
    return arr


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(0, board)
print(answer)

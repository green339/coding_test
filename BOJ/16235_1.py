# https://www.acmicpc.net/problem/16235
import sys
from collections import defaultdict

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = dict()  # 땅
tree = defaultdict(lambda: defaultdict(int))  # 나무위치, 나이
a_tmp = [list(map(int, input().split())) for _ in range(N)]
A = dict()  # S2D2
for i in range(N):
    for j in range(N):
        key = i * N + j
        board[key] = 5
        A[key] = a_tmp[i][j]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[(x - 1) * N + (y - 1)][z] = 1

for _ in range(K):
    for loc in tree.copy():
        dead = 0  # loc에서 죽는 나무들 -> 양분
        tmp = defaultdict(int)
        for age in sorted(tree[loc].keys()):
            grow = min(board[loc] // age, tree[loc][age])  # 자라는 나무
            dead += (age // 2) * (tree[loc][age] - grow)  # 죽는 나무 -> 여름에 양분
            if grow:
                board[loc] -= age * grow  # 그만큼 양분을 먹음
                tmp[age + 1] = grow
        board[loc] += dead  # 여름
        tree[loc] = tmp

    for i in range(N * N):  # 겨울
        board[i] += A[i]

    # 가을
    for loc in tree.copy():
        r, c = divmod(loc, N)
        for age in tree[loc].keys():
            if not age % 5:
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if -1 < nr < N and -1 < nc < N:
                        tree[nr * N + nc][1] += tree[loc][age]
answer = 0
for loc in tree.keys():
    for age in tree[loc]:
        answer += tree[loc][age]
print(answer)

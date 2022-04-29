# https://www.acmicpc.net/problem/21611
# 8:35
from collections import deque

direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


def move():
    full = 0
    for idx in range(1, N * N):
        if marble[idx]:
            full += 1
            if full != idx:
                marble[full] = marble[idx]
                marble[idx] = 0


def explode():
    flag = 0
    cnt = 0
    color = 0
    for idx in range(1, N * N):
        if marble[idx]:
            if marble[idx] == color:
                cnt += 1
            else:
                if cnt > 3:
                    flag = 1
                    answer[color] += cnt
                    while cnt:
                        marble[idx - cnt] = 0
                        cnt -= 1
                color = marble[idx]
                cnt = 1
        else:
            if cnt > 3:
                flag = 1
                answer[color] += cnt
                while cnt:
                    marble[idx - cnt] = 0
                    cnt -= 1
            break

    return flag


def change():
    temp = deque()
    cnt = 0
    color = 0
    for idx in range(1, N * N):
        if not marble[idx]:
            if cnt:
                temp.append(cnt)
                temp.append(color)
            break
        if marble[idx] == color:
            cnt += 1
        else:
            if cnt:
                temp.append(cnt)
                temp.append(color)
            cnt = 1
            color = marble[idx]
    for key in range(1, N * N):
        if temp:
            marble[key] = temp.popleft()
        else:
            if marble[key]:
                marble[key] = 0
            else:
                break


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]

marble = dict()
sx = N // 2
sy = N // 2
marble[0] = -1
num = 1
visited = [[0] * N for _ in range(N)]
for k in range(1, N + 1):
    dd = (-1) ** k
    for j in range(1, k + 1):
        sy += dd
        marble[num] = board[sx][sy]
        board[sx][sy] = num
        num += 1
        if num >= N * N:
            break
    else:
        for i in range(1, k + 1):
            sx -= dd
            marble[num] = board[sx][sy]
            board[sx][sy] = num
            num += 1

answer = {1: 0, 2: 0, 3: 0}
for d, s in magic:
    # 구슬 파괴
    nx = N // 2
    ny = N // 2
    while s:
        nx += direction[d][0]
        ny += direction[d][1]
        if -1 < nx < N and -1 < ny < N:
            marble[board[nx][ny]] = 0
        s -= 1
    # 구슬 폭발
    is_explode = 1
    while is_explode:
        move()
        is_explode = explode()
    # 구슬 변화
    change()

ans = 0
for k, v in answer.items():
    ans += k * v
print(ans)

# https://www.acmicpc.net/problem/12100
import copy


def up_right(arr):
    arr=copy.deepcopy(arr)
    for i in range(N):
        temp = []
        flag = 1
        blank = 0
        for j in range(N):
            if not arr[i][j]:
                blank += 1
                continue
            if temp and temp[-1] == arr[i][j] and flag:
                blank += 1
                temp[-1] *= 2
                flag = 0
            else:
                temp.append(arr[i][j])
                flag = 1
        for b in range(blank):
            temp.append(0)
        arr[i] = temp
    return arr


def down_left(arr):
    arr = copy.deepcopy(arr)
    for i in range(N):
        temp = []
        flag = 1
        blank = 0
        for j in range(N - 1, -1, -1):
            if not arr[i][j]:
                blank += 1
                continue
            if temp and temp[0] == arr[i][j] and flag:
                blank += 1
                temp[0] *= 2
                flag = 0
            else:
                temp.insert(0, arr[i][j])
                flag = 1
        for b in range(blank):
            temp.insert(0, 0)
        arr[i] = temp
    return arr


def dfs(depth, arr):
    global answer
    if depth == 5:
        answer = max(answer, max(map(max, arr)))
        return
    if max(map(max,arr))*2**(5-depth)<=answer:
        return
    up_arr = up_right(list(zip(*arr)))
    dfs(depth + 1, list(zip(*up_arr)))
    down_arr = down_left(list(zip(*arr)))
    dfs(depth + 1, list(zip(*down_arr)))
    left_arr = down_left(arr)
    dfs(depth + 1, left_arr)
    right_arr = up_right(arr)
    dfs(depth + 1, right_arr)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dfs(0, board)
print(answer)


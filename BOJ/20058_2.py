# https://www.acmicpc.net/problem/20058
### 회전하는 부분만 deque로 만들어봄 -> but 인접한 부분 구하기 어려움
import sys
from collections import deque

input = sys.stdin.readline


N, Q = map(int, input().split())
rc = 2 ** N
board = [list(map(int, input().split())) for _ in range(rc)]
L = list(map(int, input().split()))

for k in range(N):
    dq = deque()
    for i in range(0, rc // 2 ** k, 2):
        row = deque()
        for j in range(0, rc // 2 ** k, 2):
            tmp = deque()
            tmp.extend(list(board[i])[j:j + 2])
            tmp.extend(list(board[i + 1])[j:j + 2][::-1])
            row.append(tmp)
        dq.append(row)
    board = dq


def rotation(arr, depth):
    arr.rotate(1)
    if depth == N + 1:
        return arr
    tmp = deque()
    for a in arr:
        tmp.append(rotation(deque(a), depth + 1))
    tmp.rotate(1)
    return tmp


print(rotation(board, 3))

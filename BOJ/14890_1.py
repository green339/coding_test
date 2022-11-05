# https://www.acmicpc.net/problem/14890
# 11:19
import sys

input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for b in zip(*board):
    board.append(list(b))
answer = 0
for b in board:
    prior = b[0]
    cnt = 1
    i = 0
    while i < N - 1:
        i += 1
        if b[i] == prior:
            cnt += 1
        elif b[i] - prior == 1:
            if cnt >= L:
                prior = b[i]
                cnt = 1
            else:
                break
        elif prior - b[i] == 1:
            tmp = 0
            while i < N:
                if b[i] == prior - 1:
                    tmp += 1
                    i += 1
                else:
                    i -= 1
                    break
            if tmp >= L:
                cnt = tmp - L
                prior = b[min(i, N - 1)]
                continue
            break
        else:
            break
    else:
        answer += 1
print(answer)

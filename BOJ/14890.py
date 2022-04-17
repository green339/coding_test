# https://www.acmicpc.net/problem/14890
import sys
input = sys.stdin.readline


def check(board):
    answer = 0
    for b in board:
        prior = b[0]
        cnt = 1
        i = 1
        while i < N:
            cur = b[i]
            if cur == prior:
                cnt += 1
                i += 1
            else:
                if cur - prior == 1:
                    if cnt >= L:
                        prior = cur
                        cnt = 1
                        i += 1
                    else:
                        break
                elif prior - cur == 1:
                    if i + L <= N and len(set(b[i:i + L])) == 1:
                        i += L
                        prior = cur
                        cnt = 0
                    else:
                        break
                else:
                    break
        else:
            answer += 1
    return answer


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(check(arr) + check(list(zip(*arr))))

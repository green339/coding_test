# https://www.acmicpc.net/problem/17140
import sys
from collections import Counter

input = sys.stdin.readline


def cal(board):
    max_len = 0
    tmp = []
    for i in range(len(board)):
        tmp_r = []
        for cnt in sorted(Counter(board[i]).items(), key=lambda x: (x[1], x[0])):
            if cnt[0] == 0:
                continue
            tmp_r.extend(cnt)
        tmp.append(tmp_r)
        max_len=max(max_len,len(tmp_r))
    for i in range(len(tmp)):
        tmp[i].extend([0] * (max_len - len(tmp[i])))
        if len(tmp[i]) > 100:
            tmp[i] = tmp[i][:100]

    return max_len, tmp


if __name__ == "__main__":
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    A = [list(map(int, input().split())) for _ in range(3)]
    a_r = 3
    a_c = 3
    for t in range(102):
        if a_r > r and a_c > c and A[r][c] == k:
            break
        if a_r >= a_c:
            a_c, A = cal(A)
        else:
            a_r, A = cal(list(zip(*A)))
            A = list(zip(*A))
    print(t if t <= 100 else -1)

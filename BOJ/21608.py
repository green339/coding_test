# https://www.acmicpc.net/problem/21608
import sys

input = sys.stdin.readline
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def neighbor_empty(i, j):
    cnt = 0
    for di, dj in d:
        ni = di + i
        nj = dj + j
        if -1 < ni < N and -1 < nj < N and board[ni][nj] == 0:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    like = dict()
    for _ in range(N * N):
        tmp = list(map(int, input().split()))
        like[tmp[0]] = set(tmp[1:])
    student = dict()
    board = [[0] * N for _ in range(N)]
    satisfy = 0
    for lk, lv in like.items():
        cand1 = set()
        cand2 = set()
        cand3 = set()
        cand4 = set()
        for s in lv:
            if s in student.keys():
                sx, sy = student[s]
                for dx, dy in d:
                    nx = dx + sx
                    ny = dy + sy
                    if -1 < nx < N and -1 < ny < N and board[nx][ny] == 0:
                        if (nx, ny) in cand3:
                            cand4.add((nx, ny))
                        elif (nx, ny) in cand2:
                            cand3.add((nx, ny))
                        elif (nx, ny) in cand1:
                            cand2.add((nx, ny))
                        else:
                            cand1.add((nx, ny))
        if cand4:
            x, y = cand4.pop()
        elif cand3:
            x, y = cand3.pop()
        elif cand2:
            zero2 = -1
            x, y = 0, 0
            for r, c in sorted(cand2):
                cnt = neighbor_empty(r, c)
                if cnt > zero2:
                    zero2 = cnt
                    x, y = r, c
        elif cand1:
            zero1 = -1
            x, y = 0, 0
            for r, c in sorted(cand1):
                cnt = neighbor_empty(r, c)
                if cnt > zero1:
                    zero1 = cnt
                    x, y = r, c
        else:
            zero0 = -1
            x, y = 0, 0
            for r in range(N):
                for c in range(N):
                    if board[r][c] == 0:
                        cnt = neighbor_empty(r, c)
                        if cnt > zero0:
                            zero0 = cnt
                            x, y = r, c
        board[x][y] = lk
        student[lk] = (x, y)
    for sk, sv in student.items():
        neighbor = -1
        for dm, dn in d:
            nm = dm + sv[0]
            nn = dn + sv[1]
            if -1 < nm < N and -1 < nn < N and board[nm][nn] in like[sk]:
                neighbor += 1
        satisfy += int(10 ** neighbor)
    print(satisfy)

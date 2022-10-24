# https://www.acmicpc.net/problem/21608
import sys

input = sys.stdin.readline

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def seat(student):
    cand = set()
    max_cnt_student = -1
    for bx, by in blank:
        cnt_student = 0  # 주변에 좋아하는 사람 몇명있는지
        cnt_blank = 0  # 주변에 빈칸
        for dx, dy in d:
            nx = dx + bx
            ny = dy + by
            if -1 < nx < N and -1 < ny < N:
                if board[nx][ny] in like[student]:
                    cnt_student += 1
                elif board[nx][ny] == 0:
                    cnt_blank += 1
        if cnt_student > max_cnt_student:
            max_cnt_student = cnt_student
            cand = set()
            cand.add((-cnt_blank, bx, by))
        elif cnt_student == max_cnt_student:
            cand.add((-cnt_blank, bx, by))
        else:
            continue
    return sorted(cand)[0]


def score():
    answer = 0
    for x in range(N):
        for y in range(N):
            cnt = 0
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if -1 < nx < N and -1 < ny < N:
                    if board[nx][ny] in like[board[x][y]]:
                        cnt += 1
            if cnt:
                answer += 10 ** (cnt - 1)
    return answer


like = dict()
N = int(input())
board = [[0] * N for _ in range(N)]
blank = set([(i, j) for i in range(N) for j in range(N)])
for _ in range(N * N):
    tmp = list(map(int, input().split()))
    like[tmp[0]] = set(tmp[1:])
    res = seat(tmp[0])
    blank.remove((res[1], res[2]))
    board[res[1]][res[2]] = tmp[0]
print(score())

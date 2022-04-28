# https://www.acmicpc.net/problem/20057
# 5:00
direction = {0.01: [(-1, 1), (1, 1)],
             0.02: [(-2, 0), (2, 0)],
             0.05: [(0, -2)],
             0.07: [(-1, 0), (1, 0)],
             0.1: [(-1, -1), (1, -1)]}


def spread(d):
    global answer
    move = A[x][y]
    for k, vs in direction.items():
        tmp = int(A[x][y] * k)
        if tmp:
            for v in vs:
                move -= tmp
                if d == -1:  # 왼쪽
                    nx = x + v[0]
                    ny = y + v[1]
                elif d == 2:  # 아래
                    nx = x - v[1]
                    ny = y + v[0]
                elif d == 1:  # 오른
                    nx = x + v[0]
                    ny = y - v[1]
                elif d == -2:  # 위
                    nx = x + v[1]
                    ny = y - v[0]

                if -1 < nx < N and -1 < ny < N:
                    A[nx][ny] += tmp
                else:
                    answer += tmp
    if d == -1 and y > 0:  # 왼
        A[x][y - 1] += move
    elif d == 1 and y < N - 1:  # 오른
        A[x][y + 1] += move
    elif d == 2 and x < N - 1:  # 아래
        A[x + 1][y] += move
    elif d == -2 and x > 0:  # 위
        A[x - 1][y] += move
    else:
        answer += move
    A[x][y] = 0


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0
cnt = 1
x = N // 2
y = N // 2 - 1
spread(-1)
while cnt < N:
    flag = (-1) ** (cnt + 1)
    # 열 움직임
    for _ in range(cnt):  # 위 아래
        x += flag
        spread(2 * flag)
    cnt += 1
    for _ in range(cnt):  # 왼 오
        y += flag
        if y == -1:
            break
        spread(1 * flag)

print(answer)

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
direction = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


def tour(x, y, ch):
    global ans
    if ch == 3 and x == i and y == j:  # 원점으로 돌아오는 경우
        ans = max(ans, sum(cafe))
        return
    if -1 < x < N and -1 < y < N and not cafe[board[x][y]]:
        # 직진
        nx = x + direction[ch][0]
        ny = y + direction[ch][1]
        cafe[board[x][y]] = 1
        tour(nx, ny, ch)
        cafe[board[x][y]] = 0
        # 꺾는 경우
        if ch < 3:
            nx = x + direction[ch + 1][0]
            ny = y + direction[ch + 1][1]
            cafe[board[x][y]] = 1
            tour(nx, ny, ch + 1)
            cafe[board[x][y]] = 0


answer = dict()
T = int(input())
for tc in range(1, T + 1):
    ans = -1
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            cafe = [0] * 101
            tour(i, j, 0)
    answer[tc] = ans

for k, v in answer.items():
    print(f"#{k} {v}")

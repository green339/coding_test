# https://www.acmicpc.net/problem/17825

def dfs(depth, temp, start, m):
    global answer
    if start > 0:  # 중복해서 하는 경우 제외
        return
    if depth == len(order):
        answer = max(temp, answer)
        return
    move = order[depth]
    for i in range(4):
        if depth == 0:
            start = i
        dx, dy = dice[i]
        if dx == -1:  # 도착한 말의 경우 제외
            continue
        cur = dy + move  # 칸만큼 움직임
        if cur < len(board[dx]):  # 도착하지 않은 경우
            tmp_dx = dx
            if dx == 0 and not board[dx][cur] % 10:  # 외곽을 돌면서 파란색 칸에 도착한 경우
                tmp_dx = board[dx][cur]
                cur = 0
            # 겹치는 부분에 도달한 경우 [25,30,35,40] //여기서는 30->31
            if cur > 0 and board[tmp_dx][cur] in cross:
                tmp_dx = board[tmp_dx][cur]
                cur = 0
            # 도착 지점에 말이 있는 경우
            if [tmp_dx, cur] in dice:
                continue

            dice[i] = [tmp_dx, cur]
            if board[tmp_dx][cur] == 31:
                dfs(depth + 1, temp + board[tmp_dx][cur] - 1, start, m + [i])
            else:
                dfs(depth + 1, temp + board[tmp_dx][cur], start, m + [i])
            dice[i] = [dx, dy]

        else:  # 도착한 경우
            dice[i] = [-1, -1]
            dfs(depth + 1, temp, start, m + [i])
            dice[i] = [dx, dy]


dice = [[0, 0] for _ in range(4)]  # 주사위 현재 위치
board = dict()
board[0] = [n for n in range(0, 41, 2)]
board[10] = [10, 13, 16, 19, 25, 31, 35, 40]
board[20] = [20, 22, 24, 25, 31, 35, 40]
board[30] = [30, 28, 27, 26, 25, 31, 35, 40]
board[25] = [25, 31, 35, 40]
board[31] = [31, 35, 40]  # 30이 겹쳐서 31
board[35] = [35, 40]
board[40] = [40]
cross = {25, 31, 35, 40}
answer = 0
order = list(map(int, input().split()))
dfs(0, 0, 0, [])
print(answer)

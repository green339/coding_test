# https://www.acmicpc.net/problem/15684

def check():
    for i in range(N):
        cur = i
        for j in range(H):
            if cur - 1 >= 0 and board[cur - 1][j]:  # 왼쪽이 1인 경우
                cur -= 1
                continue
            if board[cur][j]:  # 오른쪽이 1인 경우
                cur += 1
        if cur != i:
            return False
    return True


def dfs(depth, idx):
    global answer
    if depth >= answer:
        return
    if check():
        answer = min(answer, depth)
        return
    if depth==3:
        return
    r, c = divmod(idx, H)
    for i in range(r, N - 1):
        if i > r:
            c = 0
        for j in range(c, H):
            if not board[i][j] and not board[i+1][j]: # 자기자신과 오른쪽에 가로선 존재 X
                if i - 1 >= 0 and board[i - 1][j]:  # 왼쪽에 가로 선이 존재하는 경우
                    continue
                board[i][j] = 1
                dfs(depth + 1, i * H + j + 1)
                board[i][j] = 0


N, M, H = map(int, input().split())
board = [[0] * H for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    board[b - 1][a - 1] = 1
answer = 4
dfs(0, 0)
print(answer if answer <= 3 else -1)
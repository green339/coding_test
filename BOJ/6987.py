# https://www.acmicpc.net/problem/6987
import sys

input = sys.stdin.readline


def dfs(game):
    global flag
    if game == 15:
        # 모든 값이 0인 경우
        if not sum(sum(board, [])):
            flag = 1
        return
    # A승
    if board[A[game]][0] and board[B[game]][2]:
        board[A[game]][0] -= 1
        board[B[game]][2] -= 1
        dfs(game + 1)
        board[A[game]][0] += 1
        board[B[game]][2] += 1
    # B승
    if board[B[game]][0] and board[A[game]][2]:
        board[B[game]][0] -= 1
        board[A[game]][2] -= 1
        dfs(game + 1)
        board[B[game]][0] += 1
        board[A[game]][2] += 1
    # C승
    if board[A[game]][1] and board[B[game]][1]:
        board[A[game]][1] -= 1
        board[B[game]][1] -= 1
        dfs(game + 1)
        board[A[game]][1] += 1
        board[B[game]][1] += 1


if __name__ == "__main__":
    A = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    B = [1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5]
    cases = [list(map(int, input().split())) for _ in range(4)]
    ans = []
    global board
    board = [[0] * 3 for _ in range(6)]
    for c in cases:
        flag = 0
        for idx in range(6):
            board[idx][0] = c[3 * idx]
            board[idx][1] = c[3 * idx + 1]
            board[idx][2] = c[3 * idx + 2]

        dfs(0)
        ans.append(flag)
    print(*ans)

# https://www.acmicpc.net/problem/9663
import sys


def dfs(queen, i, N):
    cnt = 0
    if i == N:
        return 1
    for j in range(len(queen)):
        if visit[j]==1: # 같은 열에 있는 경우
            continue
        queen[i] = j  # i행 j열에 위치
        if check(queen, i):
            visit[j]=1
            cnt += dfs(queen, i + 1, N)
            visit[j] = 0
    return cnt


def check(queen, k):
    for x in range(k):
        if abs(queen[k] - queen[x]) == k - x:  # 대각선
            return 0
    return 1


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    board = [0] * N
    visit = [0]*N
    print(dfs(board, 0, N))

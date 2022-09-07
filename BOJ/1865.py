# https://www.acmicpc.net/problem/1865
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = sys.maxsize


def bf():
    dist = [INF] * (N + 1)
    dist[0] = 0
    for k in range(N):
        for i in board.keys():
            for j, c in board[i]:
                tmp = dist[i] + c
                if dist[j] > tmp:
                    if k == N - 1:
                        return True
                    dist[j] = tmp
    return False


board = defaultdict(list)
tc = int(input())
for _ in range(tc):
    board = defaultdict(list)
    N, M, W = map(int, input().split())
    for _ in range(M):
        S, E, T = map(int, input().split())
        board[S].append((E, T))
        board[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        board[S].append((E, -T))
    if bf():
        print("YES")
    else:
        print("NO")

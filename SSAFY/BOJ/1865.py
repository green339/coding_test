import sys

input = sys.stdin.readline


def bf():
    dist = [10e9] * (N + 1)
    for t in range(N):
        for s, e, c in board:
            if dist[e] > dist[s] + c:
                if t == N - 1:
                    return "YES"
                dist[e] = dist[s] + c
    return "NO"


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    board = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        board.append((S, E, T))
        board.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        board.append((S, E, -T))
    print(bf())

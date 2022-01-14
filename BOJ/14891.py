# https://www.acmicpc.net/problem/14891
import sys
from collections import deque

input = sys.stdin.readline


def right(gear, direction):
    if gear > 4 or not board[gear - 1][2] ^ board[gear][-2]:
        return
    if board[gear - 1][2] ^ board[gear][-2]:
        right(gear + 1, -direction)
        board[gear].rotate(direction)


def left(gear, direction):
    if gear < 1 or not board[gear][2] ^ board[gear + 1][-2]:
        return
    if board[gear][2] ^ board[gear + 1][-2]:
        left(gear - 1, -direction)
        board[gear].rotate(direction)


def solution():
    for w, d in rotate:
        right(w + 1, -d)
        left(w - 1, -d)
        board[w].rotate(d)


if __name__ == "__main__":
    board = dict()
    for i in range(1, 5):
        board[i] = deque(list(map(int, list(input().strip()))))
    K = int(input())
    rotate = deque([list(map(int, input().split())) for _ in range(K)])
    solution()
    ans = 0
    for idx in range(4):
        ans += (2 ** idx) * board[idx + 1][0]
    print(ans)

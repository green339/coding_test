# https://www.acmicpc.net/problem/20055
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = deque([0] * (2 * N + 1))
stage = 0
while A.count(0) < K:
    stage += 1
    A.rotate(1)
    robot.rotate(1)
    robot[N] = 0
    if robot[N - 1]:
        robot[N - 1] = 0
    for i in range(N - 2, -1, -1):
        if robot[i]:
            if A[i + 1] and not robot[i+1]:
                robot[i + 1] = 1
                robot[i] = 0
                A[i + 1] -= 1
    if A[0]:
        robot[0] = 1
        A[0] -= 1
print(stage)

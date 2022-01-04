# https://www.acmicpc.net/problem/20055
import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    length = 2 * N
    A = list(map(int, input().split()))
    step = 1
    start = 0  # 회전하는걸 이걸로 표시
    robot = [0] * length
    order = deque()
    while True:
        # 과정 1
        start = (start - 1) % length
        if robot[(start + N - 1) % length]:  # 회전해서 떨어지는 위치에 도달
            robot[(start + N - 1) % length] = 0
            order.popleft()
        # 과정 2
        cur_robot = sum(robot)
        for _ in range(cur_robot):
            idx = order.popleft()
            if A[(idx + 1) % length] and not robot[(idx + 1) % length]:
                robot[idx % length] = 0
                A[(idx + 1) % length] -= 1
                if (start + N - 1) % length == (idx + 1) % length:  # 이동해서 떨어지는 위치에 도달
                    continue
                else:
                    order.append((idx + 1) % length)
                    robot[(idx + 1) % length] = 1
            else:
                order.append(idx)
        # 과정 3
        if A[start]:
            robot[start] = 1
            A[start] -= 1
            order.append(start)
        # 과정 4
        if A.count(0) >= K:
            break
        step += 1
    print(step)


'''
# deque의 rotate를 이용해서 하는 방법
if __name__ == "__main__":
    N, K = map(int, input().split())
    A = deque(map(int, input().split()))
    step = 1
    robot = deque([0] * N)
    while True:
        # 과정1
        A.rotate(1)
        robot.rotate(1)
        robot[-1] = 0  # 회전해서 떨어지는 위치에 도달
        # 과정2
        for idx in range(N - 2, -1, -1):
            if robot[idx] and not robot[idx + 1] and A[idx + 1]:
                robot[idx] = 0
                robot[idx + 1] = 1
                A[idx + 1] -= 1
        robot[-1] = 0  # 이동해서 떨어지는 위치에 도달
        # 과정3
        if A[0]:
            robot[0] = 1
            A[0] -= 1
        # 과정4
        if A.count(0) >= K:
            break
        step += 1
    print(step)
'''
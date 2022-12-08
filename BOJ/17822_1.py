# https://www.acmicpc.net/problem/17822
import sys
from collections import deque

input = sys.stdin.readline
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def erase():
    done = 0
    for r in range(N):
        for c in range(M):
            if A[r][c] != "x":
                visited = [[0] * M for _ in range(N)]
                q = deque()
                q.append((r, c))
                todo = set()
                todo.add((r, c))
                visited[r][c] = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx = dx + x
                        ny = (dy + y) % M
                        if -1 < nx < N:
                            if not visited[nx][ny]:
                                visited[nx][ny] = 1
                                if A[nx][ny] == A[x][y]:
                                    q.append((nx, ny))
                                    todo.add((nx, ny))
                if len(todo) > 1:
                    done = 1
                    for er, ec in todo:
                        A[er][ec] = "x"
    return done


def average():
    res = 0
    numbers = set()
    for r in range(N):
        for c in range(M):
            if str(A[r][c]).isdigit():
                res += A[r][c]
                numbers.add((r, c))
    if not numbers:
        return
    avg = res / len(numbers)
    for r, c in numbers:
        if A[r][c] > avg:
            A[r][c] -= 1
        elif A[r][c] < avg:
            A[r][c] += 1


N, M, T = map(int, input().split())
A = [deque(list(map(int, input().split()))) for _ in range(N)]
for _ in range(T):
    xx, dd, kk = map(int, input().split())
    dd = 1 if not dd else -1
    rr = kk * dd
    for i in range(xx, N+1, xx):
        A[i-1].rotate(rr)
    # 인접하면서 수가 같은 것 지우기
    if not erase():
        average()
answer = 0
for i in range(N):
    for j in range(M):
        if str(A[i][j]).isdigit():
            answer += A[i][j]
print(answer)
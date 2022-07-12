# https://www.acmicpc.net/problem/14888

def dfs(depth, result):
    global max_answer, min_answer
    if depth == N:
        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)
        return
    if op[0]:
        op[0] -= 1
        dfs(depth + 1, result + A[depth])
        op[0] += 1
    if op[1]:
        op[1] -= 1
        dfs(depth + 1, result - A[depth])
        op[1] += 1
    if op[2]:
        op[2] -= 1
        dfs(depth + 1, result * A[depth])
        op[2] += 1
    if op[3]:
        op[3] -= 1
        dfs(depth + 1, int(result / A[depth]))
        op[3] += 1


N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
max_answer = -1e9
min_answer = 1e9
dfs(1,A[0])
print(max_answer)
print(min_answer)

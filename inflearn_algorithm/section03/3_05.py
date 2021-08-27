import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 투포인터
s, e = 0, 1  # 범위: s~e-1
total = A[0]
count = 0
while e <= N:
    if total >= M:
        if total == M:
            count += 1
        total -= A[s]
        s += 1
    else:
        if e < N:
            total += A[e]
        e += 1
print(count)

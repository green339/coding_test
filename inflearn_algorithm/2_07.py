import sys

N = int(sys.stdin.readline())
arr = [0, 0] + [1] * (N - 1)
for i in range(2, int(N ** 0.5) + 1):
    if not arr[i]:
        continue
    for j in range(2, N // i + 1):
        arr[i * j] = 0
prime = [k for k in range(N + 1) if arr[k]]
print(len(prime))

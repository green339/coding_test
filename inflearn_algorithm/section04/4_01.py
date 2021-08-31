import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
left = 0
right = N - 1
ans = 0
while left <= right:
    mid = (right + left) // 2
    if arr[mid] < M:
        left = mid + 1
    elif arr[mid] > M:
        right = mid - 1
    else:
        ans = mid + 1
        break
print(ans)

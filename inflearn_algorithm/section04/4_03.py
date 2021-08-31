import sys

N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

left = 0
right = sum(times)
ans = 0
max_time = max(times)
while left <= right:
    mid = (left + right) // 2
    disks = 1
    total = 0
    for t in times:
        total += t
        if total > mid:
            disks += 1
            total = t
    if disks <= M and mid >= max_time:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
